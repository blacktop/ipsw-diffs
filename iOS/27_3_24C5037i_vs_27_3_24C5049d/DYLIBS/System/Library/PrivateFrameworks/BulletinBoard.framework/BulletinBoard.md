## BulletinBoard

> `/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard`

```diff

-955.3.5.0.0
-  __TEXT.__text: 0x7c1bc
-  __TEXT.__objc_methlist: 0x8864
+955.3.9.0.0
+  __TEXT.__text: 0x7c574
+  __TEXT.__objc_methlist: 0x88b4
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x6e80
-  __TEXT.__gcc_except_tab: 0x9dc
-  __TEXT.__oslogstring: 0x6a15
+  __TEXT.__cstring: 0x6ea0
+  __TEXT.__gcc_except_tab: 0xa30
+  __TEXT.__oslogstring: 0x6aca
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__unwind_info: 0x2c80
+  __TEXT.__unwind_info: 0x2cb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x21a0
+  __DATA_CONST.__const: 0x21d0
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4178
+  __DATA_CONST.__objc_selrefs: 0x41b8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x190
-  __DATA_CONST.__got: 0x648
+  __DATA_CONST.__got: 0x650
   __AUTH_CONST.__const: 0xb40
-  __AUTH_CONST.__cfstring: 0x79e0
+  __AUTH_CONST.__cfstring: 0x7a00
   __AUTH_CONST.__objc_const: 0x10d70
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x108

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3430
-  Symbols:   5287
-  CStrings:  1557
+  Functions: 3438
+  Symbols:   5298
+  CStrings:  1560
 
Symbols:
+ +[BBSettingsAnalytics _consumeSnapshotGateWithDefaults:atDate:]
+ +[BBSettingsAnalytics _deviceSnapshotPayloadWithSectionInfo:rawSectionInfo:bulletinCountsBySectionID:globalSettings:archetypeBySectionID:deliveredQuietlyBySectionID:]
+ +[BBSettingsAnalytics _emitSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:categoriesByBundleID:error:]
+ +[BBSettingsAnalytics _isEventUsed:]
+ +[BBSettingsAnalytics _sendEvent:payload:]
+ +[BBSettingsAnalytics _sendSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:]
+ +[BBSettingsAnalytics _shouldDiscardBulletinCountsAtDate:lastSentDate:]
+ +[BBSettingsAnalytics shouldDiscardBulletinCountsWithDefaults:]
+ GCC_except_table24
+ _BBBulletinContentTypeActiveCall
+ ___156+[BBSettingsAnalytics _sendSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:]_block_invoke
+ ___156+[BBSettingsAnalytics _sendSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:]_block_invoke_2
+ ___183+[BBSettingsAnalytics _emitSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:categoriesByBundleID:error:]_block_invoke
+ ___183+[BBSettingsAnalytics _emitSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:categoriesByBundleID:error:]_block_invoke_2
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r88l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_56_e8_32s40s_e36_v32?0"NSMutableDictionary"8Q16^B24ls32l8s40l8
- +[BBSettingsAnalytics _sendSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:defaults:]
- _BBSettingsAnalyticsArchetypeForSection
- ___165+[BBSettingsAnalytics _sendSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:defaults:]_block_invoke
- ___165+[BBSettingsAnalytics _sendSnapshotWithBasePayload:silencedBySectionID:appRowSectionIDs:appRowPayloads:topicRowSectionIDs:topicRowPayloads:deviceEventUsed:defaults:]_block_invoke_2
- ___block_descriptor_89_e8_32s40s48s56s64s72s_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
CStrings:
+ "BBBulletinContentTypeActiveCall"
+ "BBSettingsAnalytics: Category lookup completion ran more than once, ignoring the repeat"
+ "BBSettingsAnalytics: No archetype recorded for a counted section, reporting it as NeverAsked"
```
