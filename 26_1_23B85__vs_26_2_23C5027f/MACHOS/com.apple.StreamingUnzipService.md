## com.apple.StreamingUnzipService

> `/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService`

```diff

-245.40.1.0.0
-  __TEXT.__text: 0x15b40
+249.0.0.0.0
+  __TEXT.__text: 0x15f84
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x2200
-  __TEXT.__objc_methlist: 0xecc
+  __TEXT.__objc_stubs: 0x2240
+  __TEXT.__objc_methlist: 0xeec
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x2f52
-  __TEXT.__oslogstring: 0x36e5
-  __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x2dbf
-  __TEXT.__objc_methtype: 0xca9
-  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__cstring: 0x2fea
+  __TEXT.__oslogstring: 0x37fe
+  __TEXT.__objc_classname: 0x20c
+  __TEXT.__objc_methname: 0x2e8b
+  __TEXT.__objc_methtype: 0xcb3
+  __TEXT.__unwind_info: 0x2d8
   __DATA_CONST.__auth_got: 0x588
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2b0
-  __DATA_CONST.__cfstring: 0x1960
+  __DATA_CONST.__cfstring: 0x19c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA.__objc_const: 0x1e30
-  __DATA.__objc_selrefs: 0xa08
-  __DATA.__objc_ivar: 0x184
+  __DATA.__objc_const: 0x1e90
+  __DATA.__objc_selrefs: 0xa20
+  __DATA.__objc_ivar: 0x18c
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x370
   __DATA.__bss: 0x98

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 243CB3D4-6EE5-3D60-A1E7-74BBEDAF7C8A
-  Functions: 301
+  UUID: FBC9B546-F6F2-31B6-BCF8-33B93AA4A25E
+  Functions: 306
   Symbols:   220
-  CStrings:  1419
+  CStrings:  1435
 
Symbols:
+ _setiopolicy_np
- _objc_retain_x28
CStrings:
+ "09:27:29"
+ "@100@0:8@16i24S28^v32@40B48B52q56@64@72@80B88^@92"
+ "@76@0:8@16i24S28^v32@40B48B52q56B64^@68"
+ "@84@0:8@16i24S28^v32B40B44q48@56B64@68^@76"
+ "Failed to clear the reserve access policy for the current thread. error: %d (%s)"
+ "Failed to set the reserve access policy for the current thread. error: %d (%s)"
+ "Missing entitlement for connection to use APFS entitled reserve space"
+ "Missing entitlement for connection to use APFS entitled reserve space : %@"
+ "Oct 18 2025"
+ "SZExtractorOptionsUsesReservePolicy"
+ "TB,N,V_usesReservePolicy"
+ "TB,R,N,V_usesReservePolicy"
+ "Using APFS entitled reserve space for path %@"
+ "_initForWritingToPath:withOpenFlags:mode:quarantineInfo:resumptionState:useFSCompression:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:reservation:usesReservePolicy:error:"
+ "_initForWritingToPath:withOpenFlags:mode:quarantineInfo:resumptionState:useFSCompression:performCachedWrites:expectedSize:usesReservePolicy:error:"
+ "_usesReservePolicy"
+ "com.apple.private.vfs.entitled-reserve-access"
+ "fileWriterForPath:withOpenFlags:mode:quarantineInfo:useFSCompression:performCachedWrites:expectedSize:asyncTrackingGroup:usesReservePolicy:errorDelegate:error:"
+ "setUsesReservePolicy:"
+ "synchronousFileWriterForPath:withOpenFlags:mode:quarantineInfo:resumptionState:useFSCompression:performCachedWrites:expectedSize:usesReservePolicy:error:"
+ "usesReservePolicy"
+ "valueForEntitlement:"
- "21:32:17"
- "@72@0:8@16i24S28^v32@40B48B52q56^@64"
- "@80@0:8@16i24S28^v32B40B44q48@56@64^@72"
- "@96@0:8@16i24S28^v32@40B48B52q56@64@72@80^@88"
- "Oct 10 2025"
- "_initForWritingToPath:withOpenFlags:mode:quarantineInfo:resumptionState:useFSCompression:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:reservation:error:"
- "_initForWritingToPath:withOpenFlags:mode:quarantineInfo:resumptionState:useFSCompression:performCachedWrites:expectedSize:error:"
- "fileWriterForPath:withOpenFlags:mode:quarantineInfo:useFSCompression:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:error:"
- "synchronousFileWriterForPath:withOpenFlags:mode:quarantineInfo:resumptionState:useFSCompression:performCachedWrites:expectedSize:error:"

```
