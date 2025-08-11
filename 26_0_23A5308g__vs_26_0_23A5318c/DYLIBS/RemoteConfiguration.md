## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-352.0.0.0.0
-  __TEXT.__text: 0x2d260
+354.0.0.0.0
+  __TEXT.__text: 0x2d328
   __TEXT.__auth_stubs: 0x9b0
   __TEXT.__objc_methlist: 0x2edc
   __TEXT.__const: 0x1ba
   __TEXT.__cstring: 0x43f5
   __TEXT.__gcc_except_tab: 0x4e8
-  __TEXT.__oslogstring: 0x1b9d
+  __TEXT.__oslogstring: 0x1b9f
   __TEXT.__swift5_typeref: 0x180
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift_as_entry: 0xc

   __TEXT.__unwind_info: 0xba0
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x564
-  __TEXT.__objc_methname: 0x82ce
-  __TEXT.__objc_methtype: 0x13b0
+  __TEXT.__objc_methname: 0x82f2
+  __TEXT.__objc_methtype: 0x13c1
   __TEXT.__objc_stubs: 0x4f60
   __DATA_CONST.__got: 0x310
   __DATA_CONST.__const: 0xfb8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: E4D8E888-53BE-3E12-A90C-469DE1EB0129
+  UUID: A6B13D2C-B6E5-3DBA-A6C7-747DBC4F0FF2
   Functions: 1331
   Symbols:   4380
-  CStrings:  2321
+  CStrings:  2322
 
Symbols:
+ -[RCConfigurationManager _endpointURLForEndpointConfig:overrideEnvironment:overrideEnabled:]
+ -[RCConfigurationManager _endpointURLForEndpointConfig:overrideEnvironment:overrideEnabled:].cold.1
+ -[RCConfigurationManager _endpointURLForEndpointConfig:overrideEnvironment:overrideEnabled:].cold.2
+ ___block_descriptor_64_e8_32s40s48bs56bs_e58_v40?0"NSDictionary"8"NSArray"16"NSArray"24"NSError"32ls32l8s48l8s40l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8
+ _objc_msgSend$_endpointURLForEndpointConfig:overrideEnvironment:overrideEnabled:
- -[RCConfigurationManager _endpointURLForEndpointConfig:]
- -[RCConfigurationManager _endpointURLForEndpointConfig:].cold.1
- -[RCConfigurationManager _endpointURLForEndpointConfig:].cold.2
- ___block_descriptor_64_e8_32s40s48bs56bs_e58_v40?0"NSDictionary"8"NSArray"16"NSArray"24"NSError"32ls48l8s32l8s40l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s72l8s56l8s64l8
- _objc_msgSend$_endpointURLForEndpointConfig:
Functions:
~ -[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:] : 2232 -> 2316
~ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_8 : 444 -> 480
~ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.112 : 564 -> 628
~ -[RCConfigurationManager _endpointURLForEndpointConfig:] -> -[RCConfigurationManager _endpointURLForEndpointConfig:overrideEnvironment:overrideEnabled:] : 376 -> 392
CStrings:
+ "@36@0:8@16Q24B32"
+ "Found endpoint URL: %{public}@ for environment: %{public}@"
+ "No endpoint URL found in the endpointConfig for environment: %{public}@"
+ "_endpointURLForEndpointConfig:overrideEnvironment:overrideEnabled:"
- "Found endpoint URL: %{public}@ for enviroment: %{public}@"
- "No endpoint URL found in the endpointConfig for enviroment: %{public}@"
- "_endpointURLForEndpointConfig:"

```
