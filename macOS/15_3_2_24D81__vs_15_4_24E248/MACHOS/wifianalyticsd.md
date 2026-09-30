## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-645.4.0.0.0
-  __TEXT.__text: 0x93aa8
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_stubs: 0x8300
-  __TEXT.__objc_methlist: 0x2ee8
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x12bb7
-  __TEXT.__gcc_except_tab: 0x4d90
-  __TEXT.__objc_methname: 0xcd5f
-  __TEXT.__oslogstring: 0x1269c
-  __TEXT.__objc_classname: 0x353
-  __TEXT.__objc_methtype: 0x10b9
+675.32.0.0.0
+  __TEXT.__text: 0x92f40
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__objc_stubs: 0x8280
+  __TEXT.__objc_methlist: 0x3178
+  __TEXT.__const: 0x128
   __TEXT.__dlopen_cstrs: 0x128
-  __TEXT.__unwind_info: 0xde8
-  __DATA_CONST.__auth_got: 0x700
+  __TEXT.__cstring: 0x12b57
+  __TEXT.__gcc_except_tab: 0x4d9c
+  __TEXT.__objc_methname: 0xcd22
+  __TEXT.__oslogstring: 0x125f8
+  __TEXT.__objc_classname: 0x31a
+  __TEXT.__objc_methtype: 0x102e
+  __TEXT.__unwind_info: 0xd90
+  __DATA_CONST.__auth_got: 0x6f0
   __DATA_CONST.__got: 0x350
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x14e0
-  __DATA_CONST.__cfstring: 0xfd00
+  __DATA_CONST.__cfstring: 0xfcc0
   __DATA_CONST.__objc_classlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0

   __DATA_CONST.__objc_dictobj: 0xf28
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x5288
-  __DATA.__objc_selrefs: 0x2b00
-  __DATA.__objc_ivar: 0x4d8
+  __DATA.__objc_const: 0x4c00
+  __DATA.__objc_selrefs: 0x2b68
+  __DATA.__objc_ivar: 0x4d0
   __DATA.__objc_data: 0x780
-  __DATA.__data: 0x488
+  __DATA.__data: 0x368
+  __DATA.__bss: 0x180
   __DATA.__common: 0x50
-  __DATA.__bss: 0x188
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/Versions/A/CoreML

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 931A13FA-FC85-3C38-A295-5C81DF2CC959
-  Functions: 1319
-  Symbols:   347
-  CStrings:  7899
+  UUID: 6F1D104B-AC17-32AD-8214-6E2D10BF2CCE
+  Functions: 1296
+  Symbols:   346
+  CStrings:  7876
 
Symbols:
+ _OBJC_CLASS_$_WADeviceAnalyticsClient
+ _kWAMessageKeyMetricDate
- _OBJC_CLASS_$_AnalyticsProcessor
- _dispatch_assert_queue$V2
- _dispatch_assert_queue_not$V2
CStrings:
+ "\"WiFiAnalytics-675.32\""
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
+ "-[WAEngine setupDeviceAnalyticsClientWithCompletionBlock:]"
+ "-[WAEngine xpcConnection:updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:]_block_invoke"
+ "3"
+ "@\"NSXPCInterface\""
+ "@\"WADeviceAnalyticsClient\""
+ "Mar  7 2025 22:20:19"
+ "T@\"NSXPCInterface\",&,N,V_exportedInterface"
+ "T@\"WADeviceAnalyticsClient\",&,V_deviceAnalyticsClient"
+ "TB,V_analyticsStoreIsReady"
+ "WiFiAnalytics-675.32"
+ "WiFiAnalytics-675.32 Mar  7 2025 22:20:16"
+ "_analyticsStoreIsReady"
+ "_deviceAnalyticsClient"
+ "_exportedInterface"
+ "_storeChangedHandler:"
+ "_updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:"
+ "analyticsStoreIsReady"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "deviceAnalyticsClient"
+ "exportedInterface"
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
- "!"
- "\"WiFiAnalytics-645.4\""
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
- "Dec 14 2024 18:49:14"
- "T@\"<WADeviceDBDelegate>\",W,N,V_dbDelegate"
- "T@\"<WADiagDBDelegate>\",W,N,V_dbDelegate"
- "T@\"<WAStreamDBDelegate>\",W,N,V_dbDelegate"
- "T@\"AnalyticsProcessor\",&,N,V_analyticsProcessor"
- "TB,N,V_analyticsProcessorIsReady"
- "WADeviceDBDelegate"
- "WADiagDBDelegate"
- "WAStreamDBDelegate"
- "WiFiAnalytics-645.4"
- "WiFiAnalytics-645.4 Dec 14 2024 18:49:09"
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
