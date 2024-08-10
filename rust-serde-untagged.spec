# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
# Check causes circular dependency (serde_untagged <-> toml)
%bcond_with check
%global debug_package %{nil}

%global crate serde-untagged

Name:           rust-serde-untagged
Version:        0.1.6
Release:        1
Summary:        Serde Visitor implementation for deserializing untagged enums
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde-untagged
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(erased-serde) >= 0.4.2 with crate(erased-serde) < 0.5.0~)
BuildRequires:  (crate(serde) >= 1.0.194 with crate(serde) < 2.0.0~)
BuildRequires:  (crate(serde/alloc) >= 1.0.194 with crate(serde/alloc) < 2.0.0~)
BuildRequires:  (crate(typeid/default) >= 1.0.0 with crate(typeid/default) < 2.0.0~)
BuildRequires:  rust >= 1.61
%if %{with check}
BuildRequires:  (crate(serde_derive/default) >= 1.0.194 with crate(serde_derive/default) < 2.0.0~)
BuildRequires:  (crate(serde_json/default) >= 1.0.110 with crate(serde_json/default) < 2.0.0~)
BuildRequires:  (crate(toml/default) >= 0.8.0 with crate(toml/default) < 0.9.0~)
%endif

%global _description %{expand:
Serde `Visitor` implementation for deserializing untagged enums.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(serde-untagged) = 0.1.6
Requires:       (crate(erased-serde) >= 0.4.2 with crate(erased-serde) < 0.5.0~)
Requires:       (crate(erased-serde/alloc) >= 0.4.2 with crate(erased-serde/alloc) < 0.5.0~)
Requires:       (crate(serde) >= 1.0.194 with crate(serde) < 2.0.0~)
Requires:       (crate(serde/alloc) >= 1.0.194 with crate(serde/alloc) < 2.0.0~)
Requires:       (crate(typeid/default) >= 1.0.0 with crate(typeid/default) < 2.0.0~)
Requires:       cargo
Requires:       rust >= 1.61

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(serde-untagged/default) = 0.1.6
Requires:       cargo
Requires:       crate(serde-untagged) = 0.1.6

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
