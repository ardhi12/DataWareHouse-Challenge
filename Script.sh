echo "Automation Script to deploy and run app inside Docker container"
echo " "
echo "Building the app"
echo " "
docker build -t dwh-cc .
echo " "
echo "Verify the image build"
echo " "
docker images
echo " "
echo "Run the Docker Container"
echo " "
docker run -it dwh-cc
echo " "
echo "Exiting the Docker automation script."