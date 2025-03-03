## BackBoardHIDEventFoundation

> `/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`

```diff

-668.4.1.0.0
-  __TEXT.__text: 0x1fed8
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x138c
+668.5.27.1.0
+  __TEXT.__text: 0x20328
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_methlist: 0x189c
   __TEXT.__const: 0xec
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__cstring: 0x22ee
-  __TEXT.__oslogstring: 0x1aed
+  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__cstring: 0x2379
+  __TEXT.__oslogstring: 0x1afd
   __TEXT.__ustring: 0x5c
-  __TEXT.__unwind_info: 0x6f8
-  __TEXT.__objc_classname: 0x729
-  __TEXT.__objc_methname: 0x3ff1
-  __TEXT.__objc_methtype: 0x153c
-  __TEXT.__objc_stubs: 0x2c60
+  __TEXT.__unwind_info: 0x730
+  __TEXT.__objc_classname: 0x725
+  __TEXT.__objc_methname: 0x4052
+  __TEXT.__objc_methtype: 0x15c6
+  __TEXT.__objc_stubs: 0x2ca0
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xda8
+  __DATA_CONST.__const: 0xe10
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe90
+  __DATA_CONST.__objc_selrefs: 0xf28
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x290
-  __AUTH_CONST.__auth_got: 0x508
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x2340
-  __AUTH_CONST.__objc_const: 0x5020
+  __AUTH_CONST.__auth_got: 0x520
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x2360
+  __AUTH_CONST.__objc_const: 0x4788
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x358
+  __DATA.__objc_ivar: 0x354
   __DATA.__data: 0x900
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0xa50
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/StudyLog.framework/StudyLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 603
-  Symbols:   958
-  CStrings:  1476
+  Functions: 614
+  Symbols:   972
+  CStrings:  1482
 
Symbols:
+ _CFAutorelease
+ _OBJC_CLASS_$_BSDescriptionStyle
+ _objc_release_x2
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_BSCompoundAssertion
CStrings:
+ "@\"NSString\"16@?0@\"BKHIDEventDeliveryManager\"8"
+ "@\"NSString\"32@0:8@\"BKSHIDEventDescriptor\"16@\"BKSHIDEventSenderDescriptor\"24"
+ "@\"NSString\"32@0:8@\"BKSHIDEventKeyCommand\"16@\"BKSHIDEventSenderDescriptor\"24"
+ "AB"
+ "_lock_asyncNotifyServicesAdded:"
+ "_lock_connection"
+ "_observeSynchronously"
+ "_startObserving:queue:sync:"
+ "copyConnection"
+ "descriptionForRootObject:withStyle:"
+ "missing queue for async case"
+ "new key command registrations for pid:%d %{public}@"
+ "no client connection for destination %{public}@"
+ "resolutionDescriptionForEventDescriptor:senderDescriptor:"
+ "resolutionDescriptionForKeyCommand:senderDescriptor:"
+ "sendEvent:toClientTaskPort:"
+ "sendEvent:toDestination:"
+ "setMaximumValueLengthBeforeTruncation:"
+ "setValueTruncation:"
+ "shouldn't be possible to be invalid here"
+ "startObservingSynchronously:"
+ "v16@?0@\"BSMutableDescriptionStyle\"8"
+ "v28@0:8^{__IOHIDEvent=}16I24"
+ "v32@0:8^{__IOHIDEvent=}16@24"
+ "wrong code path, pal"
- "%p disconnectionObservers"
- "1\x11\x11"
- "<%@:%p>"
- "@\"BSCompoundAssertion\""
- "@\"BSProcessDeathWatcher\""
- "@24@0:8@?16"
- "@32@0:8q16@?24"
- "T@\"BSProcessDeathWatcher\",&,N,V_processDeathWatcher"
- "_connection"
- "_observerAssertion"
- "_processDeathWatcher"
- "acquireForReason:withContext:"
- "addDisconnectionObserverBlock:"
- "addRemovalObserverForConnectionWithVersionedPID:observerBlock:"
- "assertionWithIdentifier:"
- "context"
- "new key command registrations for pid:%d env:%{public}@ token:%{public}@ %{public}@"
- "processDeathWatcher"
- "setProcessDeathWatcher:"

```
