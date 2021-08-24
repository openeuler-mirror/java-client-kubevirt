%global	package_version 0.5.0
%global	package_maven_version 0.5.0

%global	_java_jdk_home /usr/lib/jvm/java-11-openjdk

Summary:	Kubevirt java client (%{name}) for oVirt
Name:		java-client-kubevirt
Version:	0.5.0
Release:	1
License:	LGPLv2+
URL:		http://www.ovirt.org
Source:		http://resources.ovirt.org/pub/ovirt-master-snapshot/src/%{name}/%{name}-%{package_version}.tar.gz
Group:		Development/Libraries

BuildArch:	noarch

BuildRequires:	gcc
BuildRequires:	java-11-openjdk-devel >= 11.0.4
BuildRequires:	javapackages-local
BuildRequires:	maven >= 3.5.0
BuildRequires:  maven-local
BuildRequires:	maven-shade-plugin
BuildRequires:	maven-source-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-profile
BuildRequires:  maven-plugin-registry

# All are provided by our fat jar
Provides:	mvn(io.kubernetes:client-java) = 6.0.1
Provides:	mvn(io.gsonfire:gson-fire) = 1.8.3
Provides:	mvn(javax.annotation:javax.annotation-api) = 1.3.2

%description
java client kubevirt

%package javadoc
Summary:	Java-docs for %{name}
Group:		Documentation

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{package_version}

%build
%configure MVN="xmvn"
# this step is necessary to resolve mvn dependencies that are not available
# as RPM distribution
make %{?_smp_mflags}

# necessary because jdk 1.8 comes as default with xmvn
export JAVA_HOME="%{_java_jdk_home}"

%mvn_build -i -- %{?_mvn_opts}
%mvn_artifact dependency-reduced-pom.xml target/java-client-kubevirt-%{version}.jar

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Aug 17 2021 Python_Bot <Python_Bot@openeuler.org> - 0.5.0-1
- Init package
