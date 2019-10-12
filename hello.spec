###############################################################################
# Spec file for utils
################################################################################
# Configured to be built by user develop or other non-root user
################################################################################
#
Summary: Hello scripts for testing RPM creation
Name: hello
Version: 1.0.0
Release: 1
License: GPL
URL: http://www.walk8243.xyz
Group: System
Packager: walk8243


%description
A collection of hello scripts for testing RPM creation.


%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/

cp $SRC_ROOT/hello $RPM_BUILD_ROOT/usr/local/bin

exit


%files
%attr(0755, root, root) /usr/local/bin/*


%clean
rm -rf $RPM_BUILD_ROOT/usr/local/bin

# Build with the following syntax:
# export SRC_ROOT=$(pwd) && rpmbuild -bb hello.spec
