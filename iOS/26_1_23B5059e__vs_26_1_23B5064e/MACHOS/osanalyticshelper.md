## osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

-927.40.3.0.0
-  __TEXT.__text: 0x1457c
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0x2a60
-  __TEXT.__objc_methlist: 0x858
+927.40.4.0.0
+  __TEXT.__text: 0x14dcc
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_stubs: 0x2b00
+  __TEXT.__objc_methlist: 0x868
   __TEXT.__const: 0x1ca
-  __TEXT.__oslogstring: 0x1ffc
-  __TEXT.__cstring: 0x1f61
+  __TEXT.__oslogstring: 0x21ac
+  __TEXT.__cstring: 0x1fe1
   __TEXT.__objc_classname: 0x163
   __TEXT.__objc_methtype: 0x407
-  __TEXT.__gcc_except_tab: 0x7f4
-  __TEXT.__objc_methname: 0x232e
+  __TEXT.__gcc_except_tab: 0x7f8
+  __TEXT.__objc_methname: 0x23e6
   __TEXT.__constg_swiftt: 0x94
   __TEXT.__swift5_typeref: 0x78
   __TEXT.__swift5_reflstr: 0xd
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4b8
-  __DATA_CONST.__auth_got: 0x6b8
+  __TEXT.__unwind_info: 0x4c0
+  __DATA_CONST.__auth_got: 0x6d8
   __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x9a8
-  __DATA_CONST.__cfstring: 0x1b20
+  __DATA_CONST.__const: 0x9e8
+  __DATA_CONST.__cfstring: 0x1b60
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x1028
-  __DATA.__objc_selrefs: 0xbc8
+  __DATA.__objc_selrefs: 0xbf0
   __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x570
   __DATA.__data: 0x1a8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0448DBA7-5279-3ECD-8598-B20DCEA7FF97
-  Functions: 324
-  Symbols:   395
-  CStrings:  1245
+  UUID: 42A03501-9BF0-3DC4-B4F6-2146EC972A7A
+  Functions: 334
+  Symbols:   399
+  CStrings:  1268
 
Symbols:
+ _OSASafeOpenReadOnly
+ _container_system_group_path_for_identifier
+ _fchmod
+ _fchown
CStrings:
+ "Client (%d) is not entitled to set DRE opt-in."
+ "DRE opt-in operation not supported on this platform"
+ "Error getting system group container: %llu"
+ "Failed to get container path for DRE opt-in plist"
+ "Failed to set permissions for DRE opt-in plist at %@"
+ "Failed to write DRE opt-in plist to %@"
+ "Invalid DRE opt-in value for set operation"
+ "Retrieved DRE opt-in value: %d via XPC"
+ "Set DRE opt-in value to %d at %@"
+ "Unknown DRE opt-in operation: %llu"
+ "com.apple.osanalytics.dre.plist"
+ "com.apple.private.osanalytics.dre-opt-in.allow"
+ "dictionaryWithContentsOfFile:"
+ "dreOptIn"
+ "dre_optInValue"
+ "dre_optIn_operation"
+ "handleDREOptInRequestWithParams:fromConnection:forReply:"
+ "isInDeviceRecoveryEnvironment"
+ "stringWithFileSystemRepresentation:length:"
+ "v12@?0i8"
+ "writeToFile:atomically:"

```
