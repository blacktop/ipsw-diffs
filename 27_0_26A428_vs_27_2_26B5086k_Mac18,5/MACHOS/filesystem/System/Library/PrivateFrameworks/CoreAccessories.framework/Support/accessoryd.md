## accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1216.0.0.0.0
-  __TEXT.__text: 0x18b100
+1219.40.5.0.0
+  __TEXT.__text: 0x18b94c
   __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_stubs: 0x9060
   __TEXT.__objc_methlist: 0x6dbc

   __TEXT.__objc_methname: 0xfaae
   __TEXT.__objc_methtype: 0x3399
   __TEXT.__cstring: 0xe802
-  __TEXT.__oslogstring: 0x38365
+  __TEXT.__oslogstring: 0x38500
   __TEXT.__ustring: 0x232
-  __TEXT.__unwind_info: 0x63d0
-  __DATA_CONST.__const: 0x9d88
+  __TEXT.__unwind_info: 0x6408
+  __DATA_CONST.__const: 0x9f48
   __DATA_CONST.__cfstring: 0x7580
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 8226
-  Symbols:   10791
-  CStrings:  8624
+  Functions: 8239
+  Symbols:   10794
+  CStrings:  8630
 
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ ____mfi4Auth_endpoint_releaseSourceUUIDsOnCancel_block_invoke
+ ___mfi4Auth_endpoint_create_block_invoke_2
+ __mfi4Auth_endpoint_create_block_invoke_2
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
CStrings:
+ "accAuthProtocol sendAuthSetupStart (manager2): connection gone for endpointUUID %@ !!"
+ "accAuthProtocol sendAuthSetupStart timer: no endpointUUID/connectionUUID for endpoint!!"
+ "authSetupStartTimer (manager2): connection gone for endpoint %@ !!"
+ "authSetupStartTimer: no endpointUUID/connectionUUID for endpoint!!"
+ "authTimer: connection gone for endpointUUID %@, no timeout to post"
+ "authTimer: endpoint not found for endpointUUID %@ !!"
+ "timerSource: endpoint %@ already gone, nothing to close"
- "accAuthProtocol sendAuthSetupStart timer: no endpointUUID for endpoint!!"
```
