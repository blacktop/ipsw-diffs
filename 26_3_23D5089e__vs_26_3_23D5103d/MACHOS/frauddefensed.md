## frauddefensed

> `/usr/libexec/frauddefensed`

```diff

-56.6.0.0.0
-  __TEXT.__text: 0x8b488
-  __TEXT.__auth_stubs: 0x1ee0
+56.7.0.0.0
+  __TEXT.__text: 0x95ed0
+  __TEXT.__auth_stubs: 0x1f60
   __TEXT.__objc_methlist: 0x350
-  __TEXT.__const: 0x4a3c
-  __TEXT.__cstring: 0x7ac2
-  __TEXT.__swift5_typeref: 0x14b8
-  __TEXT.__swift5_capture: 0x6bc
-  __TEXT.__objc_methname: 0xdc7
+  __TEXT.__const: 0x4cd4
+  __TEXT.__cstring: 0x8072
+  __TEXT.__swift5_typeref: 0x1522
+  __TEXT.__swift5_capture: 0x6d0
+  __TEXT.__objc_methname: 0xe2b
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x16e0
+  __TEXT.__constg_swiftt: 0x1764
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x1673
-  __TEXT.__swift5_fieldmd: 0x1934
+  __TEXT.__swift5_reflstr: 0x1753
+  __TEXT.__swift5_fieldmd: 0x1a2c
   __TEXT.__swift5_assocty: 0x2f8
-  __TEXT.__swift5_proto: 0x2cc
-  __TEXT.__swift5_types: 0x1a0
-  __TEXT.__swift_as_entry: 0x164
-  __TEXT.__swift_as_ret: 0x22c
-  __TEXT.__swift5_protos: 0x40
+  __TEXT.__swift5_proto: 0x2dc
+  __TEXT.__swift5_types: 0x1a8
+  __TEXT.__swift_as_entry: 0x1b0
+  __TEXT.__swift_as_ret: 0x294
   __TEXT.__objc_classname: 0x95
   __TEXT.__objc_methtype: 0x22c
+  __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__oslogstring: 0xbf
-  __TEXT.__unwind_info: 0x1db0
-  __TEXT.__eh_frame: 0x4e68
-  __DATA_CONST.__auth_got: 0xf70
-  __DATA_CONST.__got: 0x588
-  __DATA_CONST.__auth_ptr: 0x590
-  __DATA_CONST.__const: 0x3ec8
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__unwind_info: 0x2040
+  __TEXT.__eh_frame: 0x5860
+  __DATA_CONST.__auth_got: 0xfb0
+  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__auth_ptr: 0x598
+  __DATA_CONST.__const: 0x4078
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA.__objc_const: 0x1960
-  __DATA.__objc_selrefs: 0x540
-  __DATA.__objc_data: 0x980
-  __DATA.__data: 0x2dd8
+  __DATA.__objc_const: 0x1a30
+  __DATA.__objc_selrefs: 0x560
+  __DATA.__objc_data: 0x9d0
+  __DATA.__data: 0x2ee0
   __DATA.__common: 0x178
-  __DATA.__bss: 0x4e80
+  __DATA.__bss: 0x4f80
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DF6AC47B-3AF0-376E-A62F-2AC77E1C7A84
-  Functions: 2115
-  Symbols:   796
-  CStrings:  860
+  UUID: 2B76AFD1-440F-30FF-947A-09329F52C29A
+  Functions: 2235
+  Symbols:   805
+  CStrings:  886
 
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
+ "/Library/Caches/com.apple.xbs/Sources/TrustKit/TrustKit/Source/NotificationBackgroundActivity.swift"
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
