Summary:	Fast float number parsing library (faster than strtod)
Summary(pl.UTF-8):	Szybka biblioteka analizy liczb zmiennoprzecinkowych (szybsza niż strtod)
Name:		fast_float
Version:	6.1.0
Release:	1
License:	Apache v2.0 or Boost or MIT
Group:		Development/Libraries
#Source0Download: https://github.com/fastfloat/fast_float/releases
Source0:	https://github.com/fastfloat/fast_float/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e9a548c7cc8dd0c81d620cb22c97dc40
URL:		https://github.com/fastfloat/fast_float
BuildRequires:	cmake >= 3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fast_float library provides fast header-only implementations for
the C++ from_chars functions for "float" and "double" types as well as
integer types. These functions convert ASCII strings representing
decimal values (e.g., "1.3e10") into binary types. They provide exact
rounding (including round to even).

%description -l pl.UTF-8
Biblioteka fast_float dostarcza szybkie, składające się z samych
plików nagłówkowych implementacje funkcji C++ from_chars dla typów
"float" i "double" oraz typów całkowitych. Funkcje te przekształcają
łańcuchy ASCII reprezentujące wartości dziesiętne (np. "1.3e10") na
typy binarne. Dostępne jest dokładne zaokrąglanie (w tym zaokrąglanie
do liczb parzystych).

%package devel
Summary:	Fast float number parsing library (faster than strtod)
Summary(pl.UTF-8):	Szybka biblioteka analizy liczb zmiennoprzecinkowych (szybsza niż strtod)
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7

%description devel
The fast_float library provides fast header-only implementations for
the C++ from_chars functions for "float" and "double" types as well as
integer types. These functions convert ASCII strings representing
decimal values (e.g., "1.3e10") into binary types. They provide exact
rounding (including round to even).

%description devel -l pl.UTF-8
Biblioteka fast_float dostarcza szybkie, składające się z samych
plików nagłówkowych implementacje funkcji C++ from_chars dla typów
"float" i "double" oraz typów całkowitych. Funkcje te przekształcają
łańcuchy ASCII reprezentujące wartości dziesiętne (np. "1.3e10") na
typy binarne. Dostępne jest dokładne zaokrąglanie (w tym zaokrąglanie
do liczb parzystych).

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS LICENSE-BOOST LICENSE-MIT
%{_includedir}/fast_float
%{_datadir}/cmake/FastFloat
