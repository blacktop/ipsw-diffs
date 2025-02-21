## AppleConvergedFirmwareUpdater

> `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater`

```diff

-434.0.0.0.0
-  __TEXT.__text: 0x29558
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__const: 0x7784
-  __TEXT.__gcc_except_tab: 0x1b74
-  __TEXT.__cstring: 0x8cb6
+447.0.0.0.0
+  __TEXT.__text: 0x2d240
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__const: 0x77c7
+  __TEXT.__gcc_except_tab: 0x1ca8
+  __TEXT.__cstring: 0x9043
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__unwind_info: 0xf30
   __TEXT.__objc_methname: 0x4b
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0xab0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0xba0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x670
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0xfb8
-  __AUTH_CONST.__cfstring: 0xac0
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__auth_ptr: 0x18
+  __AUTH_CONST.__const: 0xf80
+  __AUTH_CONST.__cfstring: 0xb00
   __DATA.__data: 0x28
-  __DATA.__bss: 0x80
-  __DATA_DIRTY.__bss: 0xc70
+  __DATA.__bss: 0x68
+  __DATA_DIRTY.__bss: 0xc88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 720
-  Symbols:   1337
-  CStrings:  976
+  Functions: 1046
+  Symbols:   1701
+  CStrings:  1003
 
Symbols:
+ _CFDataCreateCopy
+ __ZN12ACFUFTABFile13moveFileToTopERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN12ACFURTKitROM19copyManifestSigCertEPK8__CFData
+ __ZN13RTKitFirmware12moveTagToTopERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN22ACFURTKitNVRMGenerator12copyVariableENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN7ACFUFDR16getDictLocalCopyERKNS_6ConfigEPKcty
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _oidQCCompliance
+ _oidQCDisclosures
+ _oidQCEuRetentionPeriod
+ _oidQCLimitValue
+ _oidQCStatements
+ _oidQCSyntaxv1
+ _oidQCSyntaxv2
+ _oidQCType
+ _oidQCTypeEseal
+ _oidQCTypeEsign
+ _oidQCTypeWeb
+ _oidSemanticsIdEidasLegal
+ _oidSemanticsIdEidasNatural
+ _oidSemanticsIdLegal
+ _oidSemanticsIdNatural
- __ZN10ACFUCommon27getSystemGroupContainerPathEPKc
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- _container_system_group_path_for_identifier
CStrings:
+ "%s::%s: %s already at top\n"
+ "%s::%s: beginning manifest offset mismatch: %u != %ld\n"
+ "%s::%s: didn't find requested tag\n"
+ "%s::%s: failed to allocate dataIntance, dataClass\n"
+ "%s::%s: failed to create data\n"
+ "%s::%s: failed to create new data\n"
+ "%s::%s: failed to decode manifest: %d\n"
+ "%s::%s: failed to get dict from local FDR data store\n"
+ "%s::%s: failed to get manifest length\n"
+ "%s::%s: failed to get manifest start\n"
+ "%s::%s: failed to reinit cache\n"
+ "%s::%s: first file offset mismatch: %u < %ld\n"
+ "%s::%s: invalid sig cert length\n"
+ "%s::%s: moving %s to top\n"
+ "%s::%s: no dataref\n"
+ "%s::%s: no digest in build ID (%s)\n"
+ "%s::%s: no manifest\n"
+ "%s::%s: optional tag %s missing from build identity, skipping\n"
+ "%s::%s: sig cert start falls after end of manifest\n"
+ "%s::%s: sig cert start falls before start of manifest\n"
+ "%s::%s: tag %s missing from firmware, skipping\n"
+ "%s::%s: wrong digest type (%s)\n"
+ "%s::%s: wrong type, expected dict\n"
+ "FDRUseEngineering"
+ "copyManifestSigCert"
+ "createRequest: no digest in build ID"
+ "createRequest: wrong digest type"
+ "getDictLocalCopy"
+ "moveFileToTop"
+ "moveTagToTop"
+ "sikManifestSigCert.bin"
- "%s::%s: Tag '%s' doesn't exist -- moving along\n"
- "%s::%s: error getting system group container: %llu\n"
- "%s::%s: system group container path: %s\n"
- "getSystemGroupContainerPath"

```
