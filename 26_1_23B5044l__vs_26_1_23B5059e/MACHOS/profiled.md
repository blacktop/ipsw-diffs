## profiled

> `/usr/libexec/profiled`

```diff

-2430.0.0.0.0
-  __TEXT.__text: 0xc0bec
+2432.40.1.0.0
+  __TEXT.__text: 0xc0f5c
   __TEXT.__auth_stubs: 0x2840
-  __TEXT.__objc_stubs: 0x105e0
-  __TEXT.__objc_methlist: 0x6054
+  __TEXT.__objc_stubs: 0x10600
+  __TEXT.__objc_methlist: 0x605c
   __TEXT.__const: 0x117e
   __TEXT.__gcc_except_tab: 0x1c3c
   __TEXT.__oslogstring: 0xfb20
   __TEXT.__cstring: 0xa36a
-  __TEXT.__objc_methname: 0x15fd4
+  __TEXT.__objc_methname: 0x16009
   __TEXT.__objc_classname: 0xbd5
   __TEXT.__objc_methtype: 0x2315
   __TEXT.__constg_swiftt: 0xd0c

   __TEXT.__unwind_info: 0x1ab0
   __TEXT.__eh_frame: 0x158
   __DATA_CONST.__auth_got: 0x1430
-  __DATA_CONST.__got: 0x1fe0
+  __DATA_CONST.__got: 0x1fe8
   __DATA_CONST.__auth_ptr: 0x220
   __DATA_CONST.__const: 0x2d60
   __DATA_CONST.__cfstring: 0x8680

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x6e80
-  __DATA.__objc_selrefs: 0x51e0
+  __DATA.__objc_const: 0x6e88
+  __DATA.__objc_selrefs: 0x51e8
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x1ea8
   __DATA.__data: 0x8e8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C587AF5B-49EB-3F2D-AE5D-B28D94CD9051
+  UUID: E9DAD2E9-9B5A-3A6C-8A2F-08E12EE7F308
   Functions: 2596
-  Symbols:   1758
-  CStrings:  6732
+  Symbols:   1759
+  CStrings:  6734
 
Symbols:
+ _MCFeatureAppsRatingExemptedBundleIDs
+ _MCFeatureLegacyAppsRatingExemptedBundleIDs
- _OBJC_CLASS_$_MDMUserConfiguration
Functions:
~ sub_100014c8c : 156 -> 180
~ sub_100014d28 -> sub_100014d40 : 608 -> 632
~ sub_100014f88 -> sub_100014fb8 : 564 -> 588
~ sub_1000151bc -> sub_100015204 : 564 -> 588
~ sub_1000153f0 -> sub_100015450 : 564 -> 588
~ sub_100015624 -> sub_10001569c : 564 -> 588
~ sub_1000397b0 -> sub_100039840 : 1600 -> 2204
~ sub_100040aa0 -> sub_100040d8c : 1272 -> 1292
~ sub_100052144 -> sub_100052444 : 928 -> 1020
~ sub_100084658 -> sub_1000849b4 : 1848 -> 1868
CStrings:
+ "MCInstaller checking for MDM profile..."
+ "MCInstaller could not find an MDM profile. Removing MDM-related files..."
+ "MCInstaller finished checking for MDM profile"
+ "MCInstaller uprooting MDM"
+ "awaitStoredProfileInstallationWithCompletionHandler:"
- "MCInstaller checking for MDM installation..."
- "MCInstaller could not find an MDM installation. Removing MDM-related files..."
- "MCInstaller finished checking for MDM installation"

```
