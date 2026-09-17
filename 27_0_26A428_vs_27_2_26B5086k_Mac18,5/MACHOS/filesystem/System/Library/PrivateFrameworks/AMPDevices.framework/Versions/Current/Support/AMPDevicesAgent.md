## AMPDevicesAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/Current/Support/AMPDevicesAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1.7.0.161.2
-  __TEXT.__text: 0x663050
-  __TEXT.__auth_stubs: 0x5900
+1.7.1.18.1
+  __TEXT.__text: 0x663958
+  __TEXT.__auth_stubs: 0x5910
   __TEXT.__objc_stubs: 0x8300
   __TEXT.__init_offsets: 0x90
   __TEXT.__objc_methlist: 0x1f34
   __TEXT.__const: 0x85b08
-  __TEXT.__gcc_except_tab: 0x2b01c
-  __TEXT.__cstring: 0x604e8
-  __TEXT.__oslogstring: 0x1c576
-  __TEXT.__objc_methname: 0x8e2b
+  __TEXT.__gcc_except_tab: 0x2b170
+  __TEXT.__cstring: 0x60647
+  __TEXT.__oslogstring: 0x1c6f1
+  __TEXT.__objc_methname: 0x8e3d
   __TEXT.__objc_classname: 0x374
   __TEXT.__objc_methtype: 0x28fd
-  __TEXT.__unwind_info: 0x15fb8
+  __TEXT.__unwind_info: 0x15fe8
   __TEXT.__eh_frame: 0x1c0
-  __DATA_CONST.__const: 0x54028
-  __DATA_CONST.__cfstring: 0x13e00
+  __DATA_CONST.__const: 0x540b0
+  __DATA_CONST.__cfstring: 0x13e60
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x2c98
+  __DATA_CONST.__auth_got: 0x2ca0
   __DATA_CONST.__got: 0xec8
   __DATA_CONST.__auth_ptr: 0x198
   __DATA.__objc_const: 0x2268
-  __DATA.__objc_selrefs: 0x2798
+  __DATA.__objc_selrefs: 0x27a0
   __DATA.__objc_ivar: 0x110
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x1ab8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17933
-  Symbols:   1939
-  CStrings:  19812
+  Functions: 17940
+  Symbols:   1940
+  CStrings:  19828
 
Symbols:
+ __ZNSt3__111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE
CStrings:
+ "(outChangeDataVar->mValidFields & kAMPLPlaylistChangeDataValidField_Var_ArtworkVariantsInfo) != kAMPLPlaylistChangeDataValidFields_Var_None"
+ "**ERROR**: Aborting attempts to create & register client:%s with clientID:%u"
+ "**ERROR**: Failed to Validate() ClientCommandProcessor::Command supplied to EnqueueCommand()! failure: %{public}s ClientCommandType:%d ccp:%{public}s"
+ "**ERROR**: InitGetDomainInfo() failed! status:%d"
+ "**ERROR**: InitOpenDomains() failed! failed! status:%d"
+ "**ERROR**: mLibraryClient = [[AMPLMediaAppClient alloc] initWithClientInfo:%{public}s] failed! error:%{public}@"
+ "1.7.1"
+ "1.7.1.18"
+ "13.7.1"
+ "13.7.1.18"
+ "AMPDevicesAgent: 1.7.1.18"
+ "ArtworkVariantsInfo"
+ "ExpectedInitialDFU"
+ "Missing mData when requiresData is true"
+ "amd"
+ "amplc> retrying creating & registering client:%s with clientID:%u"
+ "artwork-variants-info"
+ "artworkVariantsInfo"
+ "batteryInfo != nullptr"
+ "inCommand.Validate(failureReason)"
+ "mFireDelayTime < 0"
+ "mType == eUnknownCommandValue"
+ "systemYellowColor"
- "**ERROR**: Failed to Validate() ClientCommandProcessor::Command supplied to EnqueueCommand()! ClientCommandType:%d ccp:%{public}s"
- "1.7"
- "1.7.0.161"
- "13.7"
- "13.7.0.161"
- "AMPDevicesAgent: 1.7.0.161"
- "inCommand.Validate()"
```
