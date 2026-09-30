## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1402.300.158.2.2
-  __TEXT.__text: 0x2874bc
+1402.300.164.2.2
+  __TEXT.__text: 0x287ae0
   __TEXT.__auth_stubs: 0x43b0
-  __TEXT.__objc_methlist: 0x1273c
+  __TEXT.__objc_methlist: 0x1276c
   __TEXT.__const: 0x2fc8
-  __TEXT.__cstring: 0x129d1
-  __TEXT.__gcc_except_tab: 0x26820
-  __TEXT.__oslogstring: 0x449f7
+  __TEXT.__cstring: 0x12a21
+  __TEXT.__gcc_except_tab: 0x268dc
+  __TEXT.__oslogstring: 0x44c47
   __TEXT.__ustring: 0x37a
   __TEXT.__dlopen_cstrs: 0xfa
   __TEXT.__constg_swiftt: 0x108c

   __TEXT.__swift5_proto: 0x1e8
   __TEXT.__swift5_types: 0x114
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0xab60
+  __TEXT.__unwind_info: 0xaba0
   __TEXT.__eh_frame: 0x1fe8
   __TEXT.__objc_classname: 0x2da1
-  __TEXT.__objc_methname: 0x44b85
-  __TEXT.__objc_methtype: 0x9117
-  __TEXT.__objc_stubs: 0x2bd60
-  __DATA_CONST.__got: 0x2a48
-  __DATA_CONST.__const: 0x5c90
+  __TEXT.__objc_methname: 0x44e82
+  __TEXT.__objc_methtype: 0x9120
+  __TEXT.__objc_stubs: 0x2bf80
+  __DATA_CONST.__got: 0x2a70
+  __DATA_CONST.__const: 0x5cd8
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x5f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd178
+  __DATA_CONST.__objc_selrefs: 0xd210
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x4f0
-  __DATA_CONST.__objc_arraydata: 0xb0
+  __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x21e8
   __AUTH_CONST.__auth_ptr: 0x9d0
-  __AUTH_CONST.__const: 0x54b8
-  __AUTH_CONST.__cfstring: 0xe140
-  __AUTH_CONST.__objc_const: 0x21a18
+  __AUTH_CONST.__const: 0x54d8
+  __AUTH_CONST.__cfstring: 0xe0c0
+  __AUTH_CONST.__objc_const: 0x21b28
   __AUTH_CONST.__objc_intobj: 0x918
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x2448
   __AUTH.__data: 0x5a0
-  __DATA.__objc_ivar: 0xe50
+  __DATA.__objc_ivar: 0xe64
   __DATA.__data: 0x4670
   __DATA.__bss: 0x3900
   __DATA.__common: 0xf0

   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9817
-  Symbols:   2670
-  CStrings:  17562
+  Functions: 9826
+  Symbols:   2675
+  CStrings:  17593
 
Symbols:
+ _CGSizeZero
+ _IMChatPropertyLastMessage
+ _IMChatPropertyMergedPinningIdentifiers
+ _IMFileTransferAttributionInfoPreviewGenerationPendingKey
+ _IMPreviewGenerationFailedNotificationName
+ _IMPreviewGenerationSucceededNotificationName
+ _IMPreviewGenerationSucceededNotificationSizeUserInfoKey
+ _IMPreviewGenerationVersion
+ _IMServicePropertiesFromIMServiceBundle
+ _IMShouldReindexUTITypeWithPreviewGenerationState
+ _IMStringFromCGSize
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
- _FZServicePropertyDefaultBuddyListDescription
- _FZServicePropertyLocalizableDomain
- _FZServicePropertyShortName
- _IMDefaultServiceCapabilities
- _IMDefaultServiceHybridCapabilities
- _IMServicePropertyHybridCapabilities
- _IMServiceRegionCapabilities
- _MGGetStringAnswer
CStrings:
+ "\x02\x15\x11\x14"
+ "%!@(MISSING) is not running in the background"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"RBSProcessMonitor\""
+ "Finished re-indexing %!l(MISSING)d messages due to preview generation state change"
+ "Marking transfer %!@(MISSING) as succeeding preview generation"
+ "Preview generation failed for transfer %!@(MISSING), but ignoring due to override"
+ "Preview generation succeeded for transfer %!@(MISSING), but ignoring due to override"
+ "Re-indexing %!l(MISSING)d messages due to preview generation state change"
+ "T@\"NSMutableSet\",&,N,V_messagesToReindexForPreviewGeneration"
+ "Transfer GUID %!@(MISSING) from message %!@(MISSING) should be re-indexed due to preview generation state change"
+ "Transfer GUID %!@(MISSING) should be re-indexed due to preview generation state change, but has not been persisted to the database yet. It will be indexed once the message is stored."
+ "_canSend"
+ "_flushMessagesToReindexForPreviewGeneration"
+ "_messagesToReindexForPreviewGeneration"
+ "_migratePreviewGenerationState"
+ "_previewGenerationFailedNotification:"
+ "_previewGenerationSucceededNotification:"
+ "_processMonitor"
+ "_processMonitorDeliveredFirstUpdate"
+ "_processMonitorWaitingForInitialStateGroup"
+ "_reindexTransferIfNeededForPreviewGenerationStateChange:originalPreviewGenerationState:"
+ "_updateTransferPreviewGenerationState:newState:"
+ "com.apple.frontboard.visibility"
+ "descriptor"
+ "endowmentNamespaces"
+ "generatePreview:previewURL:senderContext:constraints:balloonBundleID:transferGUID:completionBlock:blockUntilReply:"
+ "generatePreviewForTransfer:messageItem:senderContext:"
+ "getValue:size:"
+ "ignorePreviewGenerationNotifications"
+ "messagesToReindexForPreviewGeneration"
+ "monitorWithConfiguration:"
+ "previewGenerationState"
+ "setEndowmentNamespaces:"
+ "setMessagesToReindexForPreviewGeneration:"
+ "setPredicates:"
+ "setPreviewGenerationState:"
+ "setPreviewGenerationVersion:"
+ "setStateDescriptor:"
+ "setUpdateHandler:"
+ "setValues:"
+ "successfullyGeneratedPreviewForTransfer:"
+ "successfullyGeneratedPreviewForTransfer:withPreviewSize:"
+ "taskState"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
+ "v40@0:8@\"NSString\"16{CGSize=dd}24"
+ "v40@0:8@16{CGSize=dd}24"
- "\x02\x18"
- "\a"
- "Applying capability overrides for region %!@(MISSING)"
- "Lazuli"
- "Satellite"
- "_applyDefaultsToServiceCapabilitiesWithProperties:"
- "_applyRegionOverridesToServiceCapabilitiesWithProperties:"
- "_clientPreviewConstraints"
- "_copyServicePropertiesFromIMServiceBundle:"
- "_transcodeControllerSharedInstance"
- "generatePreview:previewURL:senderContext:constraints:balloonBundleID:completionBlock:blockUntilReply:"
- "h63QSdBCiT/z0WU6rdQv6Q"
- "mergedPinningIdentifiers"
- "updateTransfer:withPreviewSize:forConstraints:"
- "v72@0:8@16@24{IMPreviewConstraints=d{CGSize=dd}dBBB}32"
- "{IMPreviewConstraints=d{CGSize=dd}dBBB}16@0:8"

```
