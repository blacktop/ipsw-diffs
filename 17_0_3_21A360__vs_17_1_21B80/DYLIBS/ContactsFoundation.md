## ContactsFoundation

> `/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation`

```diff

-1231.0.0.0.0
-  __TEXT.__text: 0x7d55c
+1232.0.0.0.0
+  __TEXT.__text: 0x7dd8c
   __TEXT.__auth_stubs: 0x1790
-  __TEXT.__objc_methlist: 0x92c8
-  __TEXT.__cstring: 0x6c1b
+  __TEXT.__objc_methlist: 0x9330
+  __TEXT.__cstring: 0x6c4b
   __TEXT.__const: 0x3a8
   __TEXT.__oslogstring: 0x1cf8
-  __TEXT.__gcc_except_tab: 0x102c
+  __TEXT.__gcc_except_tab: 0x10bc
   __TEXT.__ustring: 0x2e2
   __TEXT.__dlopen_cstrs: 0xb5
   __TEXT.__swift5_typeref: 0x150

   __TEXT.__swift5_fieldmd: 0xdc
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x3038
+  __TEXT.__unwind_info: 0x3060
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x1fa0
-  __TEXT.__objc_methname: 0x11aa9
-  __TEXT.__objc_methtype: 0x2d0b
-  __TEXT.__objc_stubs: 0xcc60
+  __TEXT.__objc_classname: 0x1fae
+  __TEXT.__objc_methname: 0x11c63
+  __TEXT.__objc_methtype: 0x2d20
+  __TEXT.__objc_stubs: 0xcdc0
   __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x3518
-  __DATA_CONST.__objc_classlist: 0x910
+  __DATA_CONST.__const: 0x3548
+  __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xefc8
-  __DATA_CONST.__objc_selrefs: 0x4630
+  __DATA_CONST.__objc_const: 0xf050
+  __DATA_CONST.__objc_selrefs: 0x4698
   __DATA_CONST.__objc_arraydata: 0x9c90
-  __AUTH_CONST.__cfstring: 0xa680
-  __AUTH_CONST.__objc_const: 0x61d8
-  __AUTH_CONST.__const: 0x1f30
+  __AUTH_CONST.__cfstring: 0xa6a0
+  __AUTH_CONST.__objc_const: 0x6220
+  __AUTH_CONST.__const: 0x1f50
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__objc_dictobj: 0x2580
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH.__objc_data: 0x2ab0
+  __AUTH.__objc_data: 0x2b00
   __AUTH.__data: 0xf8
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x930
-  __DATA.__objc_superrefs: 0x548
-  __DATA.__objc_ivar: 0x794
+  __DATA.__objc_superrefs: 0x550
+  __DATA.__objc_ivar: 0x798
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1908
   __DATA.__bss: 0x2c8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4298
-  Symbols:   14253
-  CStrings:  5558
+  Functions: 4307
+  Symbols:   14294
+  CStrings:  5577
 
Symbols:
+ +[CNFoundationError errorWithCode:underlyingException:]
+ -[CNRetry .cxx_destruct]
+ -[CNRetry delegate]
+ -[CNRetry initWithDelegate:]
+ -[CNRetry init]
+ -[CNRetry performAndWait:]
+ -[CNTask(Retry) runWithRetryDelegate:]
+ _CNContactsFoundationUnderlyingExceptionKey
+ _OBJC_CLASS_$_CNRetry
+ _OBJC_IVAR_$_CNRetry._delegate
+ _OBJC_METACLASS_$_CNRetry
+ __OBJC_$_CLASS_METHODS_CNTask(Retry)
+ __OBJC_$_INSTANCE_METHODS_CNRetry
+ __OBJC_$_INSTANCE_METHODS_CNTask(Retry)
+ __OBJC_$_INSTANCE_VARIABLES_CNRetry
+ __OBJC_$_PROP_LIST_CNRetry
+ __OBJC_CLASS_RO_$_CNRetry
+ __OBJC_METACLASS_RO_$_CNRetry
+ ___26-[CNRetry performAndWait:]_block_invoke
+ ___38-[CNTask(Retry) runWithRetryDelegate:]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_"CNResult"8?0ls32l8
+ _objc_msgSend$errorWithCode:underlyingException:
+ _objc_msgSend$maximumNumberOfAttemptsForRetry:
+ _objc_msgSend$performAndWait:
+ _objc_msgSend$retry:delayAfterError:onAttempt:
+ _objc_msgSend$retry:delayAfterException:onAttempt:
+ _objc_msgSend$retry:didCompleteAttempt:
+ _objc_msgSend$retry:didDelayFor:afterAttempt:
+ _objc_msgSend$retry:didSucceedWithResult:
+ _objc_msgSend$retry:shouldContinueAfterError:onAttempt:
+ _objc_msgSend$retry:shouldContinueAfterException:onAttempt:
+ _objc_msgSend$retry:willBeginAttempt:
+ _objc_msgSend$retry:willDelayFor:afterAttempt:
- __OBJC_$_CLASS_METHODS_CNTask
- __OBJC_$_INSTANCE_METHODS_CNTask
- _objc_msgSend$weakProxyWithObject:
CStrings:
+ "@\"<CNRetryDelegate>\""
+ "@\"CNResult\"8@?0"
+ "CNRetry"
+ "Retry"
+ "T@\"<CNRetryDelegate>\",R,W,V_delegate"
+ "com.apple.contacts.underlying-exception"
+ "errorWithCode:underlyingException:"
+ "maximumNumberOfAttemptsForRetry:"
+ "performAndWait:"
+ "retry:delayAfterError:onAttempt:"
+ "retry:delayAfterException:onAttempt:"
+ "retry:didCompleteAttempt:"
+ "retry:didDelayFor:afterAttempt:"
+ "retry:didSucceedWithResult:"
+ "retry:shouldContinueAfterError:onAttempt:"
+ "retry:shouldContinueAfterException:onAttempt:"
+ "retry:willBeginAttempt:"
+ "retry:willDelayFor:afterAttempt:"
+ "runWithRetryDelegate:"

```
