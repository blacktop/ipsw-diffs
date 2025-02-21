## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-700.2.0.0.0
-  __TEXT.__text: 0x86208
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_stubs: 0x8400
-  __TEXT.__objc_methlist: 0x2f18
+725.33.0.0.0
+  __TEXT.__text: 0x85704
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_stubs: 0x8360
+  __TEXT.__objc_methlist: 0x3190
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x12cc6
-  __TEXT.__gcc_except_tab: 0x4d74
-  __TEXT.__objc_methname: 0xce63
-  __TEXT.__oslogstring: 0x1267f
-  __TEXT.__objc_classname: 0x353
-  __TEXT.__objc_methtype: 0x10d0
   __TEXT.__dlopen_cstrs: 0x17a
-  __TEXT.__unwind_info: 0xdb8
-  __DATA_CONST.__auth_got: 0x7b0
+  __TEXT.__cstring: 0x12c73
+  __TEXT.__gcc_except_tab: 0x4d74
+  __TEXT.__objc_methname: 0xcdda
+  __TEXT.__oslogstring: 0x125db
+  __TEXT.__objc_classname: 0x31a
+  __TEXT.__objc_methtype: 0x1033
+  __TEXT.__unwind_info: 0xd68
+  __DATA_CONST.__auth_got: 0x7a0
   __DATA_CONST.__got: 0x378
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x12c0
-  __DATA_CONST.__cfstring: 0xfd40
+  __DATA_CONST.__cfstring: 0xfd00
   __DATA_CONST.__objc_classlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0

   __DATA_CONST.__objc_dictobj: 0xf28
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x52d8
-  __DATA.__objc_selrefs: 0x2b48
-  __DATA.__objc_ivar: 0x4e0
+  __DATA.__objc_const: 0x4c20
+  __DATA.__objc_selrefs: 0x2ba8
+  __DATA.__objc_ivar: 0x4d4
   __DATA.__objc_data: 0x780
-  __DATA.__data: 0x488
-  __DATA.__common: 0x50
+  __DATA.__data: 0x368
   __DATA.__bss: 0x1c8
+  __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1262
-  Symbols:   374
-  CStrings:  5905
+  Functions: 1238
+  Symbols:   373
+  CStrings:  5880
 
Symbols:
+ _OBJC_CLASS_$_WADeviceAnalyticsClient
+ _kWAMessageKeyMetricDate
- _OBJC_CLASS_$_AnalyticsProcessor
- _dispatch_assert_queue$V2
- _dispatch_assert_queue_not$V2
CStrings:
+ "\x01\x14"
+ "\x16\x11\x11"
+ "\"WiFiAnalytics_executables-725.33\""
+ "%@/%@.%@"
+ "%{public}s::%d:Already processed 50 store json files, waiting for next timer"
+ "%{public}s::%d:AnalyticsStore not ready"
+ "%{public}s::%d:AnalyticsStore ready after first unlock"
+ "%{public}s::%d:Got keyBagLockStateChangeNotification isKeyBagUnlocked is true, attempting to loadStore"
+ "%{public}s::%d:Ignoring and removing stale (%.2f days old) Store json file %@ containing %@"
+ "%{public}s::%d:Initialize DeviceAnalyticsClient"
+ "%{public}s::%d:Not running _triggerQueryForNWActivity due to _isAssociatedStateKnown %d shouldExecuteGetter %d"
+ "%{public}s::%d:Received Notification %@"
+ "%{public}s::%d:Result for triggerDeviceAnalyticsStoreMigrationAndReply via XPC - Store not ready and keybag locked"
+ "%{public}s::%d:Store not ready yet"
+ "%{public}s::%d:Unable to load AnalyticsStore. Will not be processing any metrics!"
+ "-[WAEngine _storeChangedHandler:]"
+ "-[WAEngine _updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:]_block_invoke"
+ "-[WAEngine setupDeviceAnalyticsClientWithCompletionBlock:]_block_invoke"
+ "-[WAEngine xpcConnection:updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:]_block_invoke"
+ "4"
+ "@\"WADeviceAnalyticsClient\""
+ "Feb 16 2025 05:09:03"
+ "T@\"WADeviceAnalyticsClient\",&,N,V_deviceAnalyticsClient"
+ "TB,N,V_analyticsStoreIsReady"
+ "WiFiAnalytics_executables-725.33"
+ "WiFiAnalytics_executables-725.33 Feb 16 2025 05:09:01"
+ "_analyticsStoreIsReady"
+ "_deviceAnalyticsClient"
+ "_storeChangedHandler:"
+ "_updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:"
+ "analyticsStoreIsReady"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "deviceAnalyticsClient"
+ "getPolicyHandlersConfig"
+ "isWritingInAnalyticsStoreAllowed"
+ "processWAMessageMetric:data:andDeferSaveToDisk:"
+ "setAnalyticsStoreIsReady:"
+ "setDeviceAnalyticsClient:"
+ "setPolicyHandlersConfig:"
+ "setupDeviceAnalyticsClientWithCompletionBlock:"
+ "sharedDeviceAnalyticsClient"
+ "storeLoaded"
+ "updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:"
+ "xpcConnection:updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16"
- "\x01$"
- "!"
- "\"WiFiAnalytics_executables-700.2\""
- "%@%@.%@"
- "%{public}s::%d:Alloc AnalyticsProcessor with AnalyticsProcessorMigrationCapable"
- "%{public}s::%d:AnalyticsProcessor nil"
- "%{public}s::%d:AnalyticsProcessor not ready yet"
- "%{public}s::%d:AnalyticsProcessor ready after first unlock"
- "%{public}s::%d:Got keyBagLockStateChangeNotification isKeyBagUnlocked is true, attempting setup setupAnalyticsProcessorWithCompletionBlock"
- "%{public}s::%d:Result for triggerDeviceAnalyticsStoreMigrationAndReply via XPC - AnalyticsProcessor ready"
- "%{public}s::%d:Roam Samples %lu "
- "%{public}s::%d:Unable to alloc analyticsProcessor. Will not be processing any metrics for AnalyticsStore!"
- "%{public}s::%d:Updated deploymentMetricDiffDays to %lu days"
- "%{public}s::%d:Updated testDateDiffDays to %lu days"
- "%{public}s::%d:[WAUtil shouldEnableXPCStore] true, also setting AnalyticsProcessorEnableXPCStore"
- "%{public}s::%d:analyticsProcessor nil"
- "%{public}s::%d:analyticsProcessor nil. processImmediately=%d"
- "&\x11\x11"
- "-[WAEngine _summarizeDeviceAnalyticsForNetwork:maxAgeInDays:]_block_invoke"
- "-[WAEngine processMetricDictOnEngine:data:]"
- "-[WAEngine setupAnalyticsProcessorWithCompletionBlock:]_block_invoke"
- "-[WAEngine storeWAMessageToDB:]"
- "-[WAEngine xpcConnection:summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:]_block_invoke"
- "@\"<WADeviceDBDelegate>\""
- "@\"<WADiagDBDelegate>\""
- "@\"<WAStreamDBDelegate>\""
- "@\"AnalyticsProcessor\""
- "AnalyticsProcessor: Process Metric"
- "AnalyticsProcessor: Save WA Message Metric"
- "D"
- "Jan 16 2025 04:01:30"
- "T@\"<WADeviceDBDelegate>\",W,N,V_dbDelegate"
- "T@\"<WADiagDBDelegate>\",W,N,V_dbDelegate"
- "T@\"<WAStreamDBDelegate>\",W,N,V_dbDelegate"
- "T@\"AnalyticsProcessor\",&,N,V_analyticsProcessor"
- "TB,N,V_analyticsProcessorIsReady"
- "WADeviceDBDelegate"
- "WADiagDBDelegate"
- "WAStreamDBDelegate"
- "WiFiAnalytics_executables-700.2"
- "WiFiAnalytics_executables-700.2 Jan 16 2025 04:01:27"
- "_analyticsProcessor"
- "_analyticsProcessorIsReady"
- "_dbDelegate"
- "_summarizeDeviceAnalyticsForNetwork:maxAgeInDays:"
- "analyticsProcessor"
- "analyticsProcessorIsReady"
- "dbDelegate"
- "deploymentMetricDiffDays"
- "initWithOptions:"
- "isAnalyticsProcessorAllowed"
- "processMetricDictOffEngine:data:"
- "processMetricDictOnEngine"
- "processMetricDictOnEngine:data:"
- "setAnalyticsProcessor:"
- "setAnalyticsProcessorIsReady:"
- "setDbDelegate:"
- "setDeploymentMetricDiffDays:"
- "setNumRoamSamples:"
- "setTestDateDiffDays:"
- "setupAnalyticsProcessorWithCompletionBlock:"
- "shouldEnableXPCStore"
- "storeWAMessageToDB"
- "storeWAMessageToDB:"
- "summarizeAnalyticsForNetwork:maxAgeInDays:"
- "testDateDiffDays"
- "v24@0:8@\"WAMessage\"16"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "xpcConnection:summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16"

```
