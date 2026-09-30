## MobileDevice

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/MobileDevice`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_MobileDev`
- `__TEXT.__dof_afc`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_classrefs`
- `__DATA.__data`

```diff

-1860.1.5.0.0
-  __TEXT.__text: 0x2b1da0
-  __TEXT.__objc_methlist: 0x3fcc
-  __TEXT.__const: 0x10e980
-  __TEXT.__cstring: 0x7ac3d
+1860.40.9.0.0
+  __TEXT.__text: 0x2b0f98
+  __TEXT.__objc_methlist: 0x3fbc
+  __TEXT.__const: 0x10e9d0
+  __TEXT.__cstring: 0x7ad97
   __TEXT.__gcc_except_tab: 0x53a4
   __TEXT.__oslogstring: 0xf37
   __TEXT.__ustring: 0xb0

   __TEXT.__dof_afc: 0x6d7
   __TEXT.__unwind_info: 0x9088
   __TEXT.__eh_frame: 0x69c
-  __TEXT.__objc_stubs: 0x5ec0
+  __TEXT.__objc_stubs: 0x5e20
   __TEXT.__auth_stubs: 0x41b0
   __TEXT.__objc_classname: 0xe2f
-  __TEXT.__objc_methname: 0x7771
+  __TEXT.__objc_methname: 0x7721
   __TEXT.__objc_methtype: 0x2782
-  __DATA_CONST.__const: 0xa798
+  __DATA_CONST.__const: 0xa7f8
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1d48
+  __DATA_CONST.__objc_selrefs: 0x1d20
   __DATA_CONST.__got: 0x3a8
-  __AUTH_CONST.__const: 0x90f0
-  __AUTH_CONST.__cfstring: 0x40420
+  __AUTH_CONST.__const: 0x90f8
+  __AUTH_CONST.__cfstring: 0x404e0
   __AUTH_CONST.__objc_const: 0x74e0
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__auth_got: 0x20d0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libssl.35.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10415
-  Symbols:   14699
-  CStrings:  16948
+  Functions: 10416
+  Symbols:   14695
+  CStrings:  16953
 
Symbols:
+ _UARPLayer2RemoteNotResponding
+ _ccmldsa_poly_bitpack_z_g1_19
+ _ccmldsa_poly_bitunpack_z_g1_19
+ _ccmldsa_poly_simplebitpack_w1_4bit
+ _getDecoderTable
+ _kAMSupportHttpOptionRequestHTTPAllowed
+ _kImg4TagStr_srvc
+ _objc_msgSend$set_atsContext:
+ _os_variant_has_internal_content
- -[AMSupportStaticURLSession shouldUpgrateToHTTPS]
- _CFBundleGetInfoDictionary
- ___49-[AMSupportStaticURLSession shouldUpgrateToHTTPS]_block_invoke
- _ccmldsa_poly_bitunpack_z
- _ccmldsa_poly_simplebitpack_w1
- _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
- _objc_msgSend$port
- _objc_msgSend$scheme
- _objc_msgSend$setPort:
- _objc_msgSend$setScheme:
- _objc_msgSend$shouldUpgrateToHTTPS
- shouldUpgrateToHTTPS.onceToken
- shouldUpgrateToHTTPS.usingATS
CStrings:
+ "-[AMSupportStaticURLSession _defaultSessionConfigurationWithIdentifier:]"
+ "1860.40.9"
+ "ATS: OS is internal."
+ "ATS: disabled per request on allowed build type."
+ "App Replacement source is being restored from backup."
+ "App Replacement source is being updated."
+ "App Replacement source is unavailable due to an in-flight install."
+ "Helsinki_Restore_Host-58.1.4"
+ "IXAppReplacementErrorDomain"
+ "NSAllowsArbitraryLoads"
+ "Pongo Hub"
+ "PongoSWD"
+ "RequestHTTPAllowed"
+ "Unhandled reason for code: %lu in domain IXAppReplacementErrorDomain"
+ "com.apple.libamsupport.amsupporturlsession"
+ "libauthinstall-1155.40.6"
+ "restore library built Sep  5 2026 at 03:58:03"
+ "set_atsContext:"
+ "usbmuxd-574"
- "-[AMSupportStaticURLSession _urlRequestForHTTPMessage:]"
- "1860.1.5"
- "Helsinki_Restore_Host-58.0.45"
- "Leaving custom port as is: %@"
- "NSAppTransportSecurity"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "libauthinstall-1155.0.5"
- "restore library built Aug  8 2026 at 12:40:30"
- "scheme"
- "setPort:"
- "setScheme:"
- "shouldUpgrateToHTTPS"
- "usbmuxd-571.0.0.0.1"
- "using ATS, upgraded requestURL to https: %@"
```
