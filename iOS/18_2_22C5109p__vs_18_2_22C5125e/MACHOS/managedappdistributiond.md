## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-2.2.25.0.0
-  __TEXT.__text: 0x56ade8
-  __TEXT.__auth_stubs: 0x55a0
+2.2.29.0.0
+  __TEXT.__text: 0x56eb38
+  __TEXT.__auth_stubs: 0x5590
   __TEXT.__objc_stubs: 0x1a80
   __TEXT.__objc_methlist: 0x1614
-  __TEXT.__const: 0x37b68
-  __TEXT.__cstring: 0xb7a5
+  __TEXT.__const: 0x37b58
+  __TEXT.__cstring: 0xb7d5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x5ed3
-  __TEXT.__oslogstring: 0xc52e
+  __TEXT.__objc_methname: 0x5ee5
+  __TEXT.__oslogstring: 0xc90e
   __TEXT.__objc_classname: 0x403
   __TEXT.__objc_methtype: 0x1558
   __TEXT.__gcc_except_tab: 0x4e8
   __TEXT.__dlopen_cstrs: 0xc8
   __TEXT.__constg_swiftt: 0x57b8
-  __TEXT.__swift5_typeref: 0x4692
+  __TEXT.__swift5_typeref: 0x46a2
   __TEXT.__swift5_proto: 0x1328
   __TEXT.__swift5_types: 0x7f0
   __TEXT.__swift5_protos: 0x6c
-  __TEXT.__unwind_info: 0xf358
-  __TEXT.__eh_frame: 0x2dc98
-  __DATA_CONST.__auth_got: 0x2ae0
-  __DATA_CONST.__got: 0x1780
-  __DATA_CONST.__auth_ptr: 0x19c0
-  __DATA_CONST.__const: 0x267b0
+  __TEXT.__unwind_info: 0xf4a8
+  __TEXT.__eh_frame: 0x2def8
+  __DATA_CONST.__auth_got: 0x2ad8
+  __DATA_CONST.__got: 0x1790
+  __DATA_CONST.__auth_ptr: 0x19d0
+  __DATA_CONST.__const: 0x26850
   __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0x170

   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x7000
-  __DATA.__objc_selrefs: 0x1918
+  __DATA.__objc_selrefs: 0x1920
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x2100
-  __DATA.__data: 0xccd8
+  __DATA.__data: 0xcd28
   __DATA.__bss: 0x25710
   __DATA.__common: 0xb80
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 14451
-  Symbols:   2498
-  CStrings:  3416
+  Functions: 14484
+  Symbols:   2499
+  CStrings:  3431
 
Symbols:
+ _$s10Foundation6LocaleV18preferredLanguagesSaySSGvgZ
+ _$s22ManagedAppDistribution21DiagnosticRequestTypeO32displayRestoreGenericMarketplaceyACSScACmFWC
+ _$s22ManagedAppDistribution21DiagnosticRequestTypeO37displayRestoreMarketplaceForPromotionyACSScACmFWC
- _$s22ManagedAppDistribution21DiagnosticRequestTypeO2eeoiySbAC_ACtFZ
- _$s7DMCApps0A6ClientVACycfC
CStrings:
+ "@@marketplaceName@@ Required"
+ "App Installation from the Web"
+ "App is supposed to be installed but unable to locate record: %!{(MISSING)public}s"
+ "Checking whether hosting app “%!s(MISSING)” was installed for development (e.g., from Xcode)…"
+ "Either we’re not running an internal OS build or the hosting app isn’t actually madctl."
+ "Handling unknown request: %!{(MISSING)public}s"
+ "Hosting app “%!s(MISSING)” is managed. Allowing MAD usage…"
+ "Hosting app “%!s(MISSING)” isn’t madctl, isn’t managed, and wasn’t installed for development. Disallowing MAD usage…"
+ "Hosting app “%!s(MISSING)” isn’t managed."
+ "Hosting app “%!s(MISSING)” was indeed installed for development. Allowing MAD usage…"
+ "Hosting app “%!s(MISSING)” wasn’t installed for development."
+ "Install @@marketplaceName@@"
+ "ManagedAppDistribution.Common.Settings"
+ "ManagedAppDistribution.NotAllowed.Title.FromWeb"
+ "No localized distributor names found for %!{(MISSING)public}s"
+ "To continue, you need to first install @@marketplaceName@@."
+ "To restore apps, you need to first install @@marketplaceName@@."
+ "Unable to obtain bundle identifier from audit token. Disallowing MAD usage…"
+ "We’re running an internal OS build, and hosting app “%!s(MISSING)” was installed with an ad-hoc code signature. Allowing MAD usage…"
+ "We’re running an internal OS build, and the “hosting app” is actually madctl. Allowing MAD usage…"
+ "[%!@(MISSING)] Localization user opted to install distributor of: %!s(MISSING)"
+ "[%!@(MISSING)] Localization user opted to install distributor: %!s(MISSING)"
+ "[%!@(MISSING)] Localization user opted to not install distributor: %!s(MISSING)"
+ "isAdHocCodeSigned"
- "Hosting app “%!s(MISSING)” isn’t managed and wasn’t installed for development."
- "Hosting app “%!s(MISSING)” isn’t managed; checking whether it was installed for development (e.g., from Xcode)…"
- "Hosting app “%!s(MISSING)” was indeed installed for development."
- "Install Marketplace"
- "ManagedAppDistribution.Settings"
- "Marketplace not Installed"
- "To install “@@appName@@” again, you need to install “@@marketplaceName@@”."
- "Unable to obtain bundle identifier from audit token"
- "“@@marketplaceName@@” needs to be installed to complete restore."

```
