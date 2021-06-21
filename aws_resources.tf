resource "aws_vpc" "myvpc" {
  cidr_block= var.vpc_cidr
  tags = {
    Name = "VPCtf"
  }
}

resource "aws_internet_gateway" "mygw" {
  vpc_id = aws_vpc.myvpc.id

  tags = {
    Name = "TGtf"
  }
}

resource "aws_subnet" "mysubnet" {
  count=length(var.AZs)
  vpc_id     = aws_vpc.myvpc.id
  map_public_ip_on_launch=true
  cidr_block = element(var.subnets_cidr,count.index)
  availability_zone = element(var.AZs,count.index)
  tags = {
    Name = "Subnet ${count.index+1}"
  }
}

resource "aws_route_table" "myroute" {
  vpc_id = aws_vpc.myvpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.mygw.id
  }

   tags = {
    Name = "Public_routeTB_tf"
  }
}

resource "aws_route_table_association" "myroute_association" {
  count = length(var.subnets_cidr)
  subnet_id      = element(aws_subnet.mysubnet.*.id,count.index)
  route_table_id = aws_route_table.myroute.id
}

resource "aws_instance" "OS1VPC" {
  ami = var.OS1Ami
  instance_type = var.OS1InstanceType
  tags = {
     Name = "My First TF OS2 launched in myvpc"
  }
  availability_zone=var.OS1AZ
  key_name =var.OS1key
  subnet_id = aws_subnet.mysubnet[0].id
}