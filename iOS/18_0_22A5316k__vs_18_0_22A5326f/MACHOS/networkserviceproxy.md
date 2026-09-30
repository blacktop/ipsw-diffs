## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-813.0.0.0.1
-  __TEXT.__text: 0xb27e8
+819.0.1.0.0
+  __TEXT.__text: 0xb2b30
   __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_stubs: 0xc540
   __TEXT.__objc_methlist: 0x3ddc
-  __TEXT.__const: 0x308
+  __TEXT.__const: 0x310
   __TEXT.__objc_methname: 0xf392
-  __TEXT.__oslogstring: 0xefe2
+  __TEXT.__oslogstring: 0xf0cb
   __TEXT.__objc_classname: 0xc61
   __TEXT.__objc_methtype: 0x2907
-  __TEXT.__gcc_except_tab: 0x4288
-  __TEXT.__cstring: 0xc0d2
+  __TEXT.__gcc_except_tab: 0x424c
+  __TEXT.__cstring: 0xc0ed
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__info_plist: 0x49b
   __TEXT.__unwind_info: 0x18d8
   __DATA_CONST.__auth_got: 0xc40
-  __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x1f18
-  __DATA_CONST.__cfstring: 0x7a00
+  __DATA_CONST.__got: 0x6a8
+  __DATA_CONST.__const: 0x1f20
+  __DATA_CONST.__cfstring: 0x7a20
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2070
-  Symbols:   620
-  CStrings:  5886
+  Symbols:   621
+  CStrings:  5890
 
Symbols:
+ _NSPOSIXErrorDomain
CStrings:
+ "Configuration start time (%!@(MISSING)) and end time (%!@(MISSING)) are not valid for configuration fetched at %!@(MISSING) (etag %!@(MISSING)), blocking fetching token keys"
+ "Configuration start time (%!@(MISSING)) and end time (%!@(MISSING)) are not valid, blocking installing oblivious config"
+ "Failed to validate configuration (new etag %!@(MISSING))"
+ "Failed to validate configuration signature (new etag %!@(MISSING))"
+ "Network connectivity error"
+ "Unable to verify configuration signature on disk (etag was %!@(MISSING))"
+ "failed to allocate signed configuration object from configuration data (new etag %!@(MISSING))"
+ "proxy configuration data changed"
+ "unable to extract wire format of configuration from signed configuration message (new etag %!@(MISSING))"
- "Configuration start time (%!@(MISSING)) and end time are not valid (%!@(MISSING)) for oblivious config, blocking"
- "Configuration start time (%!@(MISSING)) and end time are not valid (%!@(MISSING)) for token keys, blocking"
- "Unable to verify configuration signature on disk"
- "failed to allocate signed configuration object from configuration data"
- "unable to extract wire format of configuration from signed configuration message"

```
