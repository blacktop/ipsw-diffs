## IMDMessageServicesAgent

> `/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0x6f58
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x32c
-  __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x7a4
-  __TEXT.__cstring: 0x2ff
-  __TEXT.__oslogstring: 0xde7
+1481.100.29.2.9
+  __TEXT.__text: 0x76cc
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0xea0
+  __TEXT.__objc_methlist: 0x38c
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__cstring: 0x35f
+  __TEXT.__oslogstring: 0x127a
   __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methtype: 0x28c
-  __TEXT.__objc_methname: 0xe82
-  __TEXT.__unwind_info: 0x318
-  __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__objc_methname: 0x10b2
+  __TEXT.__objc_methtype: 0x2f2
+  __TEXT.__unwind_info: 0x350
   __DATA_CONST.__const: 0x360
-  __DATA_CONST.__cfstring: 0x300
+  __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x770
-  __DATA.__objc_selrefs: 0x380
-  __DATA.__objc_ivar: 0x6c
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x1d0
+  __DATA.__objc_const: 0x7d0
+  __DATA.__objc_selrefs: 0x3f0
+  __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0x140
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36347064-DADF-3CE3-BD31-56F26E67AE4E
-  Functions: 119
-  Symbols:   168
-  CStrings:  327
+  UUID: 23DBDECA-4C7C-32D2-8625-DCB303F16A6D
+  Functions: 127
+  Symbols:   177
+  CStrings:  372
 
Symbols:
+ _IMAutomaticMessageRetriesEnabled
+ _IMDMSAMaxRetryCount
+ _IMDMessageRecordCopyUnsentRetryableMessages
+ _IMDMessageServicesRoutingShouldRetrySendKey
+ _IMDMessageServicesWatchdogActionKey
+ _IMMessageSummaryInfoRCSSentOnPartiallyActiveSIM
+ _OBJC_CLASS_$_IMFeatureFlags
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _xpc_dictionary_get_bool
- _IMDMessageServicesWatchdogShouldFailSendKey
CStrings:
+ "  Skipping SMS downgrade for message %@ — still has retries (retryCount=%lld < %lld)"
+ "%s: returning NO — automatic message retries are disabled"
+ "%s: returning NO — message %@ has already been sent"
+ "%s: returning NO — message is nil"
+ "%s: returning NO — retryCount %lld has reached max (%lld) for message %@"
+ "%s: returning NO — service '%@' is not iMessage, retry not supported"
+ "%s: returning YES — message %@ on service '%@' is eligible for retry (retryCount=%lld)"
+ "-[IMDMessageServicesAgentController _shouldRetryMessage:]"
+ "@24@0:8@16"
+ "@24@0:8^{_IMDAttachmentRecordStruct={__CFRuntimeBase=QAQ}q^{__CFArray}}16"
+ "@24@0:8q16"
+ "@32@0:8@16q24"
+ "@36@0:8@16@24I32"
+ "Check watchdog for messages (networkAvailable=%d)"
+ "Message %@ (retryCount=%lld) eligible for retry on service %@"
+ "Message %@ will downgrade to SMS"
+ "Message (%@) was sent on partially active SIM, not downgrading to SMS"
+ "MessageRetryDuration"
+ "Network unavailable, skipping watchdog for message %@ instead of retrying"
+ "Routing decision for message %@: DOWNGRADE to SMS (error=%d, retryCount=%lld)"
+ "Routing decision for message %@: NO ACTION (not eligible for retry or downgrade)"
+ "Routing decision for message %@: RETRY (retryCount=%lld < %lld)"
+ "TB,R,N,GisSentOnPartiallyActiveSIM,V_sentOnPartiallyActiveSIM"
+ "Tq,R,N,V_retryCount"
+ "Watchdog signaling failure for message: %@"
+ "Watchdog signaling retry for message: %@"
+ "Watchdog: message %@ has non-retryable error %lld, skipping retry"
+ "Watchdog: message %@ has retryCount %lld < %lld, signaling retry with %0.0fs callback interval"
+ "__im_nanosecondTimeInterval"
+ "_copyUnsentMessagesWithWatermark:"
+ "_downgradeDictionaryForMessage:downgradableServices:error:"
+ "_retryCount"
+ "_retryDictionaryForMessage:"
+ "_sentOnPartiallyActiveSIM"
+ "_shouldRetryMessage:"
+ "_watchdogDictionaryForGUID:action:"
+ "addEntriesFromDictionary:"
+ "checkWatchdogWithNetworkAvailable:handler:"
+ "dateWithTimeIntervalSinceNow:"
+ "isNonBlockingAttachmentSendEnabled"
+ "isSentOnPartiallyActiveSIM"
+ "networkAvailable"
+ "numberWithInteger:"
+ "retryCount"
+ "sentOnPartiallyActiveSIM"
+ "sharedFeatureFlags"
+ "v28@0:8B16@?20"
- "@24@0:8^{_IMDAttachmentRecordStruct=}16"
- "Check watchdog for messages"
- "Chose route:%@ for message:%@"

```
