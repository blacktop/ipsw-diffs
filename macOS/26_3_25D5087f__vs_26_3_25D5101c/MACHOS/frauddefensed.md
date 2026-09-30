## frauddefensed

> `/usr/libexec/frauddefensed`

```diff

-56.6.0.0.0
-  __TEXT.__text: 0x89c14
-  __TEXT.__auth_stubs: 0x1de0
+56.7.0.0.0
+  __TEXT.__text: 0x946ac
+  __TEXT.__auth_stubs: 0x1e60
   __TEXT.__objc_methlist: 0x288
-  __TEXT.__const: 0x49cc
-  __TEXT.__cstring: 0x7cf2
+  __TEXT.__const: 0x4c34
+  __TEXT.__cstring: 0x82e2
   __TEXT.__oslogstring: 0x24f
-  __TEXT.__swift5_typeref: 0x13ea
-  __TEXT.__swift5_capture: 0x67c
-  __TEXT.__objc_methname: 0xc10
+  __TEXT.__swift5_typeref: 0x1454
+  __TEXT.__swift5_capture: 0x690
+  __TEXT.__objc_methname: 0xc74
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1698
+  __TEXT.__constg_swiftt: 0x171c
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x15d3
-  __TEXT.__swift5_fieldmd: 0x18dc
+  __TEXT.__swift5_reflstr: 0x16b3
+  __TEXT.__swift5_fieldmd: 0x19d4
   __TEXT.__swift5_assocty: 0x2f8
-  __TEXT.__swift5_proto: 0x2cc
-  __TEXT.__swift5_types: 0x19c
-  __TEXT.__swift_as_entry: 0x164
-  __TEXT.__swift_as_ret: 0x22c
-  __TEXT.__swift5_protos: 0x40
+  __TEXT.__swift5_proto: 0x2dc
+  __TEXT.__swift5_types: 0x1a4
+  __TEXT.__swift_as_entry: 0x1b0
+  __TEXT.__swift_as_ret: 0x294
   __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methtype: 0x127
+  __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1d40
-  __TEXT.__eh_frame: 0x4e10
-  __DATA_CONST.__auth_got: 0xef0
-  __DATA_CONST.__got: 0x550
-  __DATA_CONST.__auth_ptr: 0x580
-  __DATA_CONST.__const: 0x3d90
-  __DATA_CONST.__objc_classlist: 0xe0
+  __TEXT.__unwind_info: 0x1fc8
+  __TEXT.__eh_frame: 0x5808
+  __DATA_CONST.__auth_got: 0xf30
+  __DATA_CONST.__got: 0x558
+  __DATA_CONST.__auth_ptr: 0x588
+  __DATA_CONST.__const: 0x3f40
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x17a8
-  __DATA.__objc_selrefs: 0x498
-  __DATA.__objc_data: 0x930
-  __DATA.__data: 0x2ba0
+  __DATA.__objc_const: 0x1878
+  __DATA.__objc_selrefs: 0x4b8
+  __DATA.__objc_data: 0x980
+  __DATA.__data: 0x2ca8
   __DATA.__common: 0x160
-  __DATA.__bss: 0x4e80
+  __DATA.__bss: 0x4f80
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/Versions/A/CoreML

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8864C072-7D79-3423-AA77-0A82EBE117BB
-  Functions: 2085
-  Symbols:   774
-  CStrings:  806
+  UUID: 1FC4F2BE-877F-3870-9A90-C4C7B35034C4
+  Functions: 2205
+  Symbols:   783
+  CStrings:  832
 
Symbols:
+ _$s5Rules8DecisionO6ReviewyA2CmFWC
+ _$sSS10FoundationE4data8encodingSSSgAA4DataVh_SSAAE8EncodingVtcfC
+ _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeySbSgSbm_xtKF
+ _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeySdSgSdm_xtKF
+ _$ss22KeyedEncodingContainerV15encodeIfPresent_6forKeyySbSg_xtKF
+ _$ss22KeyedEncodingContainerV15encodeIfPresent_6forKeyySdSg_xtKF
+ _$ss22_minimumMergeRunLengthyS2iF
+ _$ss27_bridgeAnythingToObjectiveCyyXlxlF
+ _notify_post
CStrings:
+ "        CREATE TABLE IF NOT EXISTS CKSignatures (\n            id VARCHAR PRIMARY KEY NOT NULL,\n            signature_id VARCHAR,\n            signature BYTE,\n            signature_size INT,\n            threshold DOUBLE,\n            zone_name VARCHAR,\n            modification_date VARCHAR,\n            metadata VARCHAR\n         );"
+ ", nonMatch=nil }"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/AdHocSignaturesBackgroundActivity.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/AttestationManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/BackgroundActivityManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/CloudKitManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/CloudKitRecord.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ConfigurationsAsset.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/DaemonAnalyticsManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/DebugUIManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/EligibilityManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/JavaScriptAsset.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/LogicGraphDecisioningComponent.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/NotificationBackgroundActivity.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/RecordZonesAsset.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ReportManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ReportOperation.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ReportingAsset.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SenderLookUpDecisioningComponent.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SignatureAnalysisDecisioningComponent.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SignaturesBackgroundActivity.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SignaturesSQLiteManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SignpostsManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SpamDecisioningAsset.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SpamDecisioningManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/UAFAssetManager.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/Utility/ContainerUtility.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/Utility/KeyUtility.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/Utility/SignatureMatchUtility.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/frauddefensed/Server.swift"
+ "/AppleInternal/Library/BuildRoots/4~CGC2ugBfiph8wdLlRC5d0v1JJ6UTRIiqoNLno_U/Library/Caches/com.apple.xbs/Sources/TrustKit/frauddefensed/main.swift"
+ "/TrustKit_Signatures_v5.sqlite"
+ "Activity is already submitted. { activity=com.apple.trustkit.notification }"
+ "Activity is not already submitted. { activity="
+ "Completed notifications background system task. { taskIdentifier="
+ "Created CKSignatures table. { createQuery=        CREATE TABLE IF NOT EXISTS CKSignatures (\n            id VARCHAR PRIMARY KEY NOT NULL,\n            signature_id VARCHAR,\n            signature BYTE,\n            signature_size INT,\n            threshold DOUBLE,\n            zone_name VARCHAR,\n            modification_date VARCHAR,\n            metadata VARCHAR\n         ); }"
+ "Failed to bind metadata to query. { error="
+ "Failed to configure background activity power requirement using spam decisioning asset. { error="
+ "Failed to fetch UAF asset info for notifications background activity. { error="
+ "Failed to install notifications background activity. { error="
+ "Failed to install signatures background activity. { error="
+ "Failed to transform decision info for input features to logic graph. { error="
+ "Failed to update notifications background activity. { error="
+ "Failed to update task request. { identifier="
+ "INSERT INTO CKSignatures (id, signature_id, signature, signature_size, threshold, zone_name, modification_date, metadata) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO UPDATE SET signature_id=excluded.signature_id, signature=excluded.signature, signature_size=excluded.signature_size, threshold=excluded.threshold, zone_name=excluded.zone_name, modification_date=excluded.modification_date, metadata=excluded.metadata;"
+ "Installing notifications background task."
+ "Invalid background activity attempted to be constructed."
+ "Reinference_Background_Max_Delay"
+ "Reinference_Background_On_Power_Enabled"
+ "Reinference_Background_Schedule"
+ "Reinference_Check_Enabled"
+ "TrustKit_Signatures_v5.sqlite"
+ "Updated task request. { taskRequest="
+ "Value being transformed is not valid JSON object. { value="
+ "_TtC13frauddefensed30NotificationBackgroundActivity"
+ "com.apple.trustkit.falsepositives.notification"
+ "com.apple.trustkit.notification"
+ "isValidJSONObject:"
+ "matchedSignatures"
+ "previousDecisionInfo"
+ "randomInitialDelay"
+ "scheduleAfter"
+ "spamDecisionManagerInferenceWithOrigin:sender:messageBody:receiverISOCountryCode:attachments:trustIndicator:messageType:inferenceType:conversationState:decisionInfo:completionHandler:"
+ "updateTaskRequest:error:"
+ "v104@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSArray\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"_TtC13frauddefensed24ConversationStateWrapper\"80@\"NSDictionary\"88@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSError\">96"
+ "v104@0:8@16@24@32@40@48@56@64@72@80@88@?96"
- "        CREATE TABLE IF NOT EXISTS CKSignatures (\n            id VARCHAR PRIMARY KEY NOT NULL,\n            signature_id VARCHAR,\n            signature BYTE,\n            signature_size INT,\n            threshold DOUBLE,\n            zone_name VARCHAR,\n            modification_date VARCHAR\n         );"
- ", maximalMatchScore="
- ", maximalMatchSignatureThreshold="
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/AdHocSignaturesBackgroundActivity.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/AttestationManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/BackgroundActivityManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/CloudKitManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/CloudKitRecord.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ConfigurationsAsset.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/DaemonAnalyticsManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/DebugUIManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/EligibilityManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/JavaScriptAsset.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/LogicGraphDecisioningComponent.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/RecordZonesAsset.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ReportManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ReportOperation.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/ReportingAsset.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SenderLookUpDecisioningComponent.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SignatureAnalysisDecisioningComponent.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SignaturesBackgroundActivity.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SignaturesSQLiteManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SignpostsManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SpamDecisioningAsset.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/SpamDecisioningManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/UAFAssetManager.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/Utility/ContainerUtility.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/Utility/KeyUtility.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/Utility/SignatureMatchUtility.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/frauddefensed/Server.swift"
- "/AppleInternal/Library/BuildRoots/4~CDy4ugAzRwYD8kJOnS2qd9jUTEh8JdrfDPdmBWA/Library/Caches/com.apple.xbs/Sources/TrustKit/frauddefensed/main.swift"
- "/TrustKit_Signatures_v4.sqlite"
- "Created CKSignatures table. { createQuery=        CREATE TABLE IF NOT EXISTS CKSignatures (\n            id VARCHAR PRIMARY KEY NOT NULL,\n            signature_id VARCHAR,\n            signature BYTE,\n            signature_size INT,\n            threshold DOUBLE,\n            zone_name VARCHAR,\n            modification_date VARCHAR\n         ); }"
- "Failed to search for signature match. { input="
- "INSERT INTO CKSignatures (id, signature_id, signature, signature_size, threshold, zone_name, modification_date) VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO UPDATE SET signature_id=excluded.signature_id, signature=excluded.signature, signature_size=excluded.signature_size, threshold=excluded.threshold, zone_name=excluded.zone_name, modification_date=excluded.modification_date;"
- "Invalid background activity attempted to be submitted."
- "TrustKit_Signatures_v4.sqlite"
- "spamDecisionManagerInference:sender:messageBody:receiverISOCountryCode:attachments:trustIndicator:messageType:inferenceType:conversationState:completionHandler:"
- "v96@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSArray\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"_TtC13frauddefensed24ConversationStateWrapper\"80@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSError\">88"
- "v96@0:8@16@24@32@40@48@56@64@72@80@?88"

```
