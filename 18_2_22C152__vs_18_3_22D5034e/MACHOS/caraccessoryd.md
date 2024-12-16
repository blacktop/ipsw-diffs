## caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

-337.13.3.0.0
-  __TEXT.__text: 0x225d0
+337.16.1.0.0
+  __TEXT.__text: 0x22804
   __TEXT.__auth_stubs: 0xec0
   __TEXT.__objc_stubs: 0x1f40
   __TEXT.__objc_methlist: 0xc48
-  __TEXT.__const: 0x308
+  __TEXT.__const: 0x318
   __TEXT.__cstring: 0xdb3
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__objc_methname: 0x328d
-  __TEXT.__oslogstring: 0x303b
+  __TEXT.__objc_methname: 0x32af
+  __TEXT.__oslogstring: 0x35ab
   __TEXT.__objc_classname: 0x309
   __TEXT.__objc_methtype: 0x1043
   __TEXT.__swift5_typeref: 0x3b2

   __TEXT.__swift5_reflstr: 0x183
   __TEXT.__swift5_fieldmd: 0x1c8
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x6b8
-  __TEXT.__eh_frame: 0x138
+  __TEXT.__unwind_info: 0x6c0
+  __TEXT.__eh_frame: 0x170
   __DATA_CONST.__auth_got: 0x770
   __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0xb48
+  __DATA_CONST.__const: 0xb70
   __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x3ab0
-  __DATA.__objc_selrefs: 0xca8
+  __DATA.__objc_selrefs: 0xcb0
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x868
   __DATA.__data: 0xe28

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 683
-  Symbols:   1945
-  CStrings:  1065
+  Functions: 681
+  Symbols:   1944
+  CStrings:  1064
 
Symbols:
+ _$sSTsE5first5where7ElementQzSgSbADKXE_tKFSaySo12CAFMediaItemCG_Tg5098$s13caraccessoryd19CAFDNowPlayingAgentC09updateNowC033_FF809742895DEAA2EB5774A1CBC6B439LLyyFSbSo12dE7CXEfU0_So0D6SourceCTf1cn_nTf4ng_n
+ _$sSTsE5first5where7ElementQzSgSbADKXE_tKFSaySo17CAFMediaItemImageCG_Tg5098$s13caraccessoryd19CAFDNowPlayingAgentC09updateNowC033_FF809742895DEAA2EB5774A1CBC6B439LLyyFSbSo17deF7CXEfU1_SSTf1cn_nTf4ng_n
+ __36-[CarDataClient parseValues:errors:]_block_invoke.38
+ __36-[CarDataClient parseValues:errors:]_block_invoke.38.cold.1
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.242
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.242.cold.1
+ __49-[_CAFdConnectionProxy didUpdatePluginID:values:]_block_invoke.124
+ __68-[CarDataClient handleCommand:transactionID:values:errors:priority:]_block_invoke.42
+ __68-[CarDataClient handleCommand:transactionID:values:errors:priority:]_block_invoke.44
+ __68-[CarDataClient handleCommand:transactionID:values:errors:priority:]_block_invoke.44.cold.1
+ __68-[CarDataClient handleCommand:transactionID:values:errors:priority:]_block_invoke.44.cold.2
+ __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.252
+ __85-[CarDataClient sendCommand:values:errors:error:transactionID:priority:withResponse:]_block_invoke.32
+ ___block_descriptor_64_e8_32s40s48s56s_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8s48l8s56l8
- _$sSTsE5first5where7ElementQzSgSbADKXE_tKFSaySo17CAFMediaItemImageCG_Tg5098$s13caraccessoryd19CAFDNowPlayingAgentC09updateNowC033_FF809742895DEAA2EB5774A1CBC6B439LLyyFSbSo17deF7CXEfU0_SSTf1cn_nTf4ng_n
- __36-[CarDataClient parseValues:errors:]_block_invoke.35
- __36-[CarDataClient parseValues:errors:]_block_invoke.35.cold.1
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.240
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.240.cold.1
- __68-[CarDataClient handleCommand:transactionID:values:errors:priority:]_block_invoke.39
- __68-[CarDataClient handleCommand:transactionID:values:errors:priority:]_block_invoke.41
- __68-[CarDataClient handleCommand:transactionID:values:errors:priority:]_block_invoke.41.cold.1
- __68-[CarDataClient handleCommand:transactionID:values:errors:priority:]_block_invoke.41.cold.2
- __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.251
- __85-[CarDataClient sendCommand:values:errors:error:transactionID:priority:withResponse:]_block_invoke.29
- __85-[CarDataClient sendCommand:values:errors:error:transactionID:priority:withResponse:]_block_invoke.cold.1
- ___49-[_CAFdConnectionProxy didUpdatePluginID:values:]_block_invoke_2
CStrings:
+ "%{public}@ plugin: %{public}@ transactionID: %{public}@"
+ "%{public}@: didUpdate pluginID: %{public}@ count in: %{public}lu out: %{public}lu [%{public}@]"
+ "Add registration from cache pluginID: %{public}@ total: %ld cached: %ld [%{public}@] missing: %ld [%{public}@]"
+ "Client delegate for command: %{public}@ pluginID: %{public}@ transactionID: %{public}@ with priority: %{public}@ missing"
+ "Error parsing pluginID: %{public}@ data with error: %{public}@"
+ "Error pluginID: %{public}@ control request missing transactionID"
+ "Error pluginID: %{public}@ control response missing transactionID"
+ "Error pluginID: %{public}@ read response missing transactionID"
+ "Error pluginID: %{public}@ transactionID: %{public}@ unknown command %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong config notify values type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong config response values type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong control notify values type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong control request values type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong control response errors type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong control response values type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong read repsonse errors type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong read response values type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong register repsonse errors type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong register repsonse values type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong update data type %{public}@"
+ "Error pluginID: %{public}@ transactionID: %{public}@ wrong write response errors type %{public}@"
+ "Error pluginID: %{public}@ write response missing transactionID"
+ "Failed to generate transactionID for pluginID: %{public}@ command: %{public}@"
+ "Found media item with identifier %{public}s, frequency %{public}u"
+ "Notify pluginID: %{public}@ instanceID: %{public}@ with value: %{public}@ and priority: %{public}@"
+ "Parsing characteristic value from pluginID: %{public}@ failed with wrong instanceID data type %{public}@"
+ "Parsing characteristic value from pluginID: %{public}@ instanceID: %{public}@ failed with wrong error data type %{public}@"
+ "Parsing control notify value from pluginID: %{public}@ failed with wrong instanceID data type %{public}@"
+ "Parsing control notify value from pluginID: %{public}@ failed with wrong notification data type %{public}@"
+ "Parsing control request value from pluginID: %{public}@ failed with wrong instanceID data type %{public}@"
+ "Parsing control request value from pluginID: %{public}@ failed with wrong request data type %{public}@"
+ "Read values pluginID: %{public}@ instanceID count: %ld with priority: %{public}@"
+ "Read values pluginID: %{public}@ total: %ld from cache: %ld missing: %ld"
+ "Received characteristic value from pluginID: %{public}@ instanceID: %{public}@ with error %{public}@"
+ "Received pluginID: %{public}@ transactionID: %{public}@ config notify"
+ "Received pluginID: %{public}@ transactionID: %{public}@ config response"
+ "Received pluginID: %{public}@ transactionID: %{public}@ control notify values count: %lu"
+ "Received pluginID: %{public}@ transactionID: %{public}@ control request values count: %ld"
+ "Received pluginID: %{public}@ transactionID: %{public}@ control response values count: %ld errors count: %ld"
+ "Received pluginID: %{public}@ transactionID: %{public}@ error: %{public}@"
+ "Received pluginID: %{public}@ transactionID: %{public}@ read response values count: %ld [%{public}@] errors count: %ld [%{public}@]"
+ "Received pluginID: %{public}@ transactionID: %{public}@ register response values count: %ld errors count: %ld [%{public}@]"
+ "Received pluginID: %{public}@ transactionID: %{public}@ unregister response result: OK"
+ "Received pluginID: %{public}@ transactionID: %{public}@ update values count: %lu [%{public}@]"
+ "Received pluginID: %{public}@ transactionID: %{public}@ write response result count: %ld [%{public}@]"
+ "Remove registration from cache pluginID: %{public}@ instanceID count: %ld"
+ "Remove registration pluginID: %{public}@ instanceID count: %ld with priority: %{public}@"
+ "Request pluginID: %{public}@ add registration for instanceIDs count: %ld with priority: %{public}@"
+ "Request pluginID: %{public}@ config with priority: %{public}@"
+ "Request pluginID: %{public}@ instanceID: %{public}@ with value: %{public}@ and priority: %{public}@"
+ "Request pluginID: %{public}@ read for instanceIDs count: %ld with priority: %{public}@"
+ "Request pluginID: %{public}@ remove registration for instanceIDs count: %ld with priority: %{public}@"
+ "Request pluginID: %{public}@ to register all with priority: %{public}@"
+ "Request pluginID: %{public}@ to unregister all with priority: %{public}@"
+ "Request pluginID: %{public}@ write for values count: %ld with priority: %{public}@"
+ "Response pluginID: %{public}@ instanceID: %{public}@ control with value: %{public}@ error: %{public}@ and priority: %{public}@"
+ "Response pluginID: %{public}@ instanceID: %{public}@ transactionID: %{public}@ with error: %{public}@ and priority: %{public}@"
+ "Response pluginID: %{public}@ instanceID: %{public}@ transactionID: %{public}@ with value: %{public}@ and priority: %{public}@"
+ "Response pluginID: %{public}@ transactionID: %{public}@ with error: %{public}@ and priority: %{public}@"
+ "Send pluginID: %{public}@ command: %{public}@ transactionID: %{public}@ with priority: %{public}@ values array with %ld entries, [%{public}@]"
+ "Send pluginID: %{public}@ command: %{public}@ transactionID: %{public}@ with priority: %{public}@ values dictionary with %ld entries, [%{public}@]"
+ "Send pluginID: %{public}@ command: %{public}@ transactionID: %{public}@ with priority: %{public}@ values: %{public}@"
+ "Send pluginID: %{public}@ command: %{public}@ transactionID: %{public}@ with priority: %{public}@ without values"
+ "Unable to package command %{public}@ for pluginID: %{public}@ transactionID: %{public}@ with priority: %{public}@"
+ "Unable to send command for pluginID: %{public}@ transactionID: %{public}@ with priority: %{public}@"
+ "Unable to serialize command %{public}@ for pluginID: %{public}@ transactionID: %{public}@ with priority: %{public}@ with error: %{public}@"
+ "Write values pluginID: %{public}@ instanceID count: %ld with priority: %{public}@"
+ "currentMediaItemIdentifierInvalid"
- "%{public}@ plugin: %{public}@ transactionID: %@"
- "Add registration from cache pluginID: %@ total: %ld cached: %ld missing: %ld"
- "Add registration pluginID: %@ instanceID count: %ld with priority: %@"
- "Client delegate for pluginID: %@ transactionID: %@ with priority: %@ missing"
- "Error parsing pluginID: %@ data with error: %@"
- "Error pluginID: %@ control request missing transactionID"
- "Error pluginID: %@ control response missing transactionID"
- "Error pluginID: %@ read response missing transactionID"
- "Error pluginID: %@ transactionID: %@ unknown command %@"
- "Error pluginID: %@ transactionID: %@ wrong config notify values type %@"
- "Error pluginID: %@ transactionID: %@ wrong config response values type %@"
- "Error pluginID: %@ transactionID: %@ wrong control notify values type %@"
- "Error pluginID: %@ transactionID: %@ wrong control request values type %@"
- "Error pluginID: %@ transactionID: %@ wrong control response errors type %@"
- "Error pluginID: %@ transactionID: %@ wrong control response values type %@"
- "Error pluginID: %@ transactionID: %@ wrong read repsonse errors type %@"
- "Error pluginID: %@ transactionID: %@ wrong read response values type %@"
- "Error pluginID: %@ transactionID: %@ wrong register repsonse errors type %@"
- "Error pluginID: %@ transactionID: %@ wrong register repsonse values type %@"
- "Error pluginID: %@ transactionID: %@ wrong update data type %@"
- "Error pluginID: %@ transactionID: %@ wrong write response errors type %@"
- "Error pluginID: %@ write response missing transactionID"
- "Failed to generate transactionID for pluginID: %@ command: %@"
- "Found media item with identifier %{public}s"
- "Notify pluginID: %@ instanceID: %@ with value: %@ and priority: %@"
- "Parsing characteristic value from pluginID: %@ failed with wrong instanceID data type %@"
- "Parsing characteristic value from pluginID: %@ instanceID: %@ failed with wrong error data type %@"
- "Parsing control notify value from pluginID: %@ failed with wrong instanceID data type %@"
- "Parsing control notify value from pluginID: %@ failed with wrong notification data type %@"
- "Parsing control request value from pluginID: %@ failed with wrong instanceID data type %@"
- "Parsing control request value from pluginID: %@ failed with wrong request data type %@"
- "Read values pluginID: %@ instanceID count: %ld with priority: %@"
- "Read values pluginID: %@ total: %ld from cache: %ld missing: %ld"
- "Received characteristic value from pluginID: %@ instanceID: %@ with error %@"
- "Received pluginID: %@ transactionID: %@ config notify"
- "Received pluginID: %@ transactionID: %@ config response"
- "Received pluginID: %@ transactionID: %@ control notify values count: %lu"
- "Received pluginID: %@ transactionID: %@ control request values count: %ld"
- "Received pluginID: %@ transactionID: %@ control response values count: %ld errors count: %ld"
- "Received pluginID: %@ transactionID: %@ error: %@"
- "Received pluginID: %@ transactionID: %@ read response values count: %ld errors count: %ld"
- "Received pluginID: %@ transactionID: %@ register response values count: %ld errors count: %ld"
- "Received pluginID: %@ transactionID: %@ unregister response result: OK"
- "Received pluginID: %@ transactionID: %@ update values count: %lu"
- "Received pluginID: %@ transactionID: %@ write response result count: %ld"
- "Remove registration from cache pluginID: %@ instanceID count: %ld"
- "Remove registration pluginID: %@ instanceID count: %ld with priority: %@"
- "Request pluginID: %@ add registration for instanceIDs count: %ld with priority: %@"
- "Request pluginID: %@ config with priority: %@"
- "Request pluginID: %@ instanceID: %@ with value: %@ and priority: %@"
- "Request pluginID: %@ read for instanceIDs count: %ld with priority: %@"
- "Request pluginID: %@ remove registration for instanceIDs count: %ld with priority: %@"
- "Request pluginID: %@ to register all with priority: %@"
- "Request pluginID: %@ to unregister all with priority: %@"
- "Request pluginID: %@ write for values count: %ld with priority: %@"
- "Response pluginID: %@ instanceID: %@ control with value: %@ error: %@ and priority: %@"
- "Response pluginID: %@ instanceID: %@ transactionID: %@ with error: %@ and priority: %@"
- "Response pluginID: %@ instanceID: %@ transactionID: %@ with value: %@ and priority: %@"
- "Response pluginID: %@ transactionID: %@ with error: %@ and priority: %@"
- "Send pluginID: %@ command: %@ transactionID: %@ with priority: %@ error: %@"
- "Send pluginID: %@ command: %@ transactionID: %@ with priority: %@ errors with %ld entries"
- "Send pluginID: %@ command: %@ transactionID: %@ with priority: %@ values array with %ld entries"
- "Send pluginID: %@ command: %@ transactionID: %@ with priority: %@ values dictionary with %ld entries"
- "Send pluginID: %@ command: %@ transactionID: %@ with priority: %@ values: %@"
- "Send pluginID: %@ command: %@ transactionID: %@ with priority: %@ without values"
- "Unable to package command for pluginID: %@ transactionID: %@ with priority: %@"
- "Unable to send command for pluginID: %@ transactionID: %@ with priority: %@"
- "Unable to serialize command for pluginID: %@ transactionID: %@ with priority: %@ with error: %@"
- "Write values pluginID: %@ instanceID count: %ld with priority: %@"

```
