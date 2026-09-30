## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1450.200.75.0.0
-  __TEXT.__text: 0xbc5a0
-  __TEXT.__auth_stubs: 0x1b30
+1450.200.88.2.1
+  __TEXT.__text: 0xba9ec
+  __TEXT.__auth_stubs: 0x1b50
   __TEXT.__objc_stubs: 0xc4c0
-  __TEXT.__objc_methlist: 0x2b84
-  __TEXT.__const: 0xbf0
-  __TEXT.__gcc_except_tab: 0xabac
-  __TEXT.__cstring: 0x342d
-  __TEXT.__oslogstring: 0x16f96
+  __TEXT.__objc_methlist: 0x2b74
+  __TEXT.__const: 0xc50
+  __TEXT.__gcc_except_tab: 0xabdc
+  __TEXT.__cstring: 0x344d
+  __TEXT.__oslogstring: 0x16c5b
   __TEXT.__objc_classname: 0x548
-  __TEXT.__objc_methname: 0x1262f
-  __TEXT.__objc_methtype: 0x2955
+  __TEXT.__objc_methname: 0x12665
+  __TEXT.__objc_methtype: 0x29ca
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x662
-  __TEXT.__constg_swiftt: 0x38c
-  __TEXT.__swift5_reflstr: 0x2b0
-  __TEXT.__swift5_fieldmd: 0x35c
-  __TEXT.__swift5_proto: 0x38
+  __TEXT.__swift5_typeref: 0x668
+  __TEXT.__constg_swiftt: 0x368
+  __TEXT.__swift5_reflstr: 0x2d6
+  __TEXT.__swift5_fieldmd: 0x368
+  __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x3c
   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x44

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x22e0
-  __TEXT.__eh_frame: 0x930
-  __DATA_CONST.__auth_got: 0xda8
-  __DATA_CONST.__got: 0xff0
-  __DATA_CONST.__auth_ptr: 0x170
+  __TEXT.__unwind_info: 0x22c8
+  __TEXT.__eh_frame: 0x8d8
+  __DATA_CONST.__auth_got: 0xdb8
+  __DATA_CONST.__got: 0x1010
+  __DATA_CONST.__auth_ptr: 0x1b8
   __DATA_CONST.__const: 0x38b0
   __DATA_CONST.__cfstring: 0x37e0
   __DATA_CONST.__objc_classlist: 0xf0

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x32a8
+  __DATA.__objc_const: 0x3240
   __DATA.__objc_selrefs: 0x3a28
-  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_ivar: 0x208
   __DATA.__objc_data: 0xa58
-  __DATA.__data: 0xa50
-  __DATA.__bss: 0x7d0
+  __DATA.__data: 0xa38
+  __DATA.__bss: 0x8d0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8EC057F3-FD75-36F7-B571-41E76ACAD8D9
-  Functions: 1666
-  Symbols:   864
-  CStrings:  5102
+  UUID: 72FB8926-7965-3BFF-B5E2-5B30499B3815
+  Functions: 1659
+  Symbols:   866
+  CStrings:  5090
 
Symbols:
+ _IMMetricsAttachmentDownloadAttachmentFailureReasonAutodownloadLimitExceeded
+ _IMMetricsAttachmentDownloadAttachmentFailureReasonInternalOverride
+ _IMMetricsAttachmentDownloadAttachmentFailureReasonOutOfStorage
+ _OBJC_CLASS_$_IMAttachmentDownloadMetricsContext
- _IMDisableFilteringProcessing
- _IMInternationalForPhoneNumberWithOptions
CStrings:
+ "@\"IMAttachmentDownloadMetricsContext\""
+ "@60@0:8Q16Q24Q32B40B44B48@52"
+ "Not notifying coreroutined about incoming CheckIn(messageGUID %@), as it's not from a known sender."
+ "T@\"IMAttachmentDownloadMetricsContext\",R,N,V_metricsContext"
+ "T@\"NSString\",R,N,V_restrictionReason"
+ "_metricsContext"
+ "_restrictionReason"
+ "collectMetricsForFailureWithReportedSize:"
+ "eligibilityController"
+ "initForServiceName:limitType:limitSize:qualityType:isSticker:lowQualityModeEnabled:"
+ "initWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:restrictionReason:"
+ "isChatConfigurationKnownWith:handles:"
+ "metricsContext"
+ "restrictionReason"
+ "restrictionWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:restrictionReason:"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "trackAttachmentDownloadFailedWithFileSize:reason:context:"
+ "trackAttachmentDownloadSuccess:context:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "%{public}s Alias is nil, but iMessage enabled: %{bool}d"
- "%{public}s Can't send over iMessage to Emergency SOS via Satellite"
- "%{public}s SIMID %s not found in registered good list"
- "%{public}s alias %s SIMID %s no longer a valid subscription, defaulting to whether iMessage is available"
- "%{public}s alias %s SIMID %s not registered but active in CT. deferring to other services"
- "%{public}s alias %s is not from an active CT subscription. set hasAccountsOnService=%{bool}d"
- "%{public}s iMessage enabled for multiple subscriptions: %{bool}d alias: %s sim: %s"
- "@52@0:8Q16Q24Q32B40B44B48"
- "No phone numbers registered - iMessage is eligible for request %s because last used service is %s"
- "No phone numbers registered - iMessage is eligible for request %s because this is a new chat"
- "No phone numbers registered - iMessage is ineligible for request %s because last used service is %s"
- "TB,R,N,V_isSticker"
- "TB,R,N,V_lqmEnabled"
- "TQ,R,N,V_limitSize"
- "TQ,R,N,V_limitType"
- "TQ,R,N,V_qualityType"
- "_isSticker"
- "_limitSize"
- "_limitType"
- "_lqmEnabled"
- "_qualityType"
- "collectMetricsForLimitExceededWithReportedSize:"
- "initWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:"
- "limitSize"
- "limitType"
- "lqmEnabled"
- "qualityType"
- "restrictionWithLimitType:limitSize:qualityType:isSticker:allowDownload:lqmEnabled:"
- "serviceOfLastMessage"
- "trackAttachmentDownloadLimitExceeded:limitSize:fileSize:qualityType:isSticker:lowQualityModeEnabled:"
- "trackAttachmentDownloadSuccess:limitType:limitSize:qualityType:isSticker:lowQualityModeEnabled:"

```
