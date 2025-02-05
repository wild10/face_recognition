# face_recognition

# Install build tools (within the virtual environment)
sudo apt-get install -y build-essential cmake git

# Download OpenCV source (within the virtual environment)
cd ~  # Or wherever you want to store the source
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout 4.11.0 # Or your desired version.  Match the one that works on your system.

# Create a build directory (within the virtual environment)
mkdir build
cd build

# Configure CMake (within the virtual environment)
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \ # Or wherever you want to install it.  Keep this consistent.
      -D WITH_GTK=ON \
      -D WITH_XINE=ON \
      -D BUILD_opencv_python3=ON \
      -D PYTHON3_EXECUTABLE=$(which python) \ # Important: Use the python in your virtual env.
      -D PYTHON3_INCLUDE_DIR=$(python -c "import sysconfig; print(sysconfig.get_path('include'))") \
      -D PYTHON3_LIBRARY=$(python -c "import sysconfig; print(sysconfig.get_path('stdlib'))") \
      ../

# Build (within the virtual environment)
make -j$(nproc)  # Use all available cores

# Install (within the virtual environment)
sudo make install

# Update the shared library cache (within the virtual environment)
sudo ldconfig
