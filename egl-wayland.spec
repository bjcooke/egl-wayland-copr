%global commit  b283689e369116aaf41ffac70d4eeef19ce133a4
%global date 20180529
%global shortcommit0 %(c=%{commit}; echo ${c:0:7})

Name:           egl-wayland
Version:        1.0.3
Release:        0.1%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:        Wayland EGL External Platform library

License:        MIT
URL:            https://github.com/NVIDIA
Source0:        %url/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source1:        10_nvidia_wayland.json

BuildRequires:  libtool
BuildRequires:  eglexternalplatform-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  wayland-devel

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
%summary

%prep
%autosetup -n %{name}-%{commit}
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static
%make_build V=1


%install
%make_install
install -m 0755 -d %{buildroot}%{_datadir}/egl/egl_external_platform.d/
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/egl/egl_external_platform.d/
rm %{buildroot}%{_libdir}/libnvidia-egl-wayland.so
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*
%{_datadir/pkgconfig/*.pc
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json


%changelog
* Tue May 29 2018 Benjamin Cooke <bcooke@freedomofknowledge.org> - 1.0.3-0.1.20180528gitb283689
- Update to 1.0.3 git

* Thu Aug 03 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-0.4.20170802git1f4b1fd
- Update to latest git snapshot

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.3.20170628git818b613
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.2.20170628git818b613
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-0.1.20170628git818b613
- Update to 1.0.2 git

* Wed Mar 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.1-0.1.20170308git582fbf3
- Update to 1.0.1 git

* Tue Feb 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.7.20170207git05eb000
- Add license file

* Thu Feb 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.6.20170120git743d702
- Add requires libglvnd-egl
- Make review changes

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.5.20170120git743d702
- Drop devel sub-package

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.4.20170120git743d702
- Add 10_nvidia_wayland.json to libs sub-package

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.3.20170120git743d702
- Add loader directory to common sub-package
- Move libs to sub-package

* Fri Jan 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.2.20170120git743d702
- Add date to release

* Fri Jan 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.1.git743d702
- First build

