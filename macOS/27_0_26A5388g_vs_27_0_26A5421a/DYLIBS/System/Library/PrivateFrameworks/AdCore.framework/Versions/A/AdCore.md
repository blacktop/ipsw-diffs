## AdCore

> `/System/Library/PrivateFrameworks/AdCore.framework/Versions/A/AdCore`

```diff

-638.1.5.0.0
-  __TEXT.__text: 0x31e1c
-  __TEXT.__objc_methlist: 0x4054
+638.1.7.0.0
+  __TEXT.__text: 0x321c0
+  __TEXT.__objc_methlist: 0x4074
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x3e46
-  __TEXT.__gcc_except_tab: 0x4ac
+  __TEXT.__cstring: 0x3ef2
+  __TEXT.__gcc_except_tab: 0x4c0
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x53
-  __TEXT.__unwind_info: 0xc08
+  __TEXT.__unwind_info: 0xc20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d8
+  __DATA_CONST.__const: 0x3f8
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fb0
+  __DATA_CONST.__objc_selrefs: 0x1fd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__got: 0x340
-  __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__cfstring: 0x4b60
-  __AUTH_CONST.__objc_const: 0x5c10
+  __AUTH_CONST.__const: 0x700
+  __AUTH_CONST.__cfstring: 0x4ba0
+  __AUTH_CONST.__objc_const: 0x5c70
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x3c8
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x3ec
+  __DATA.__objc_ivar: 0x3f8
   __DATA.__data: 0x1e0
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x240
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1429
-  Symbols:   2874
-  CStrings:  644
+  Functions: 1435
+  Symbols:   2889
+  CStrings:  646
 
Symbols:
+ -[ADCoreSettings dealloc]
+ -[ADCoreSettings invalidateAccountCache]
+ -[ADCoreSettings setIdentifierForAdvertisingAllowedCoalescedAsync:]
+ GCC_except_table16
+ GCC_except_table27
+ GCC_except_table38
+ GCC_except_table42
+ OBJC_IVAR_$_ADCoreSettings._accountCacheLock
+ OBJC_IVAR_$_ADCoreSettings._cachedIsManagedAppleID
+ OBJC_IVAR_$_ADCoreSettings._isManagedAppleIDCacheValid
+ ___67-[ADCoreSettings setIdentifierForAdvertisingAllowedCoalescedAsync:]_block_invoke
+ ___67-[ADCoreSettings setIdentifierForAdvertisingAllowedCoalescedAsync:]_block_invoke_2
+ ___block_descriptor_33_e5_v8?0l
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$setIdentifierForAdvertisingAllowedCoalescedAsync:
+ setIdentifierForAdvertisingAllowedCoalescedAsync:.identifierForAdvertisingQueue
+ setIdentifierForAdvertisingAllowedCoalescedAsync:.onceToken
- GCC_except_table36
- GCC_except_table40
- _objc_msgSend$setIdentifierForAdvertisingAllowed:
CStrings:
+ "Invalidated cached managed-Apple-ID after account change."
+ "com.apple.adcore.setIdentifierForAdvertisingAllowed"
+ "com.apple.adplatforms.UserAccountChangeCompletedNotification"
- "%F"
```
