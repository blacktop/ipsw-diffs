## BulletinBoard

> `/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard`

```diff

-921.0.0.0.0
-  __TEXT.__text: 0x80bb0
+923.0.0.0.0
+  __TEXT.__text: 0x81430
   __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x89dc
+  __TEXT.__objc_methlist: 0x8a74
   __TEXT.__const: 0x130
   __TEXT.__gcc_except_tab: 0xf78
-  __TEXT.__cstring: 0x62e8
-  __TEXT.__oslogstring: 0x6954
+  __TEXT.__cstring: 0x6315
+  __TEXT.__oslogstring: 0x6b2f
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__unwind_info: 0x2258
+  __TEXT.__unwind_info: 0x2278
   __TEXT.__objc_classname: 0xbe5
-  __TEXT.__objc_methname: 0x13b03
+  __TEXT.__objc_methname: 0x13c18
   __TEXT.__objc_methtype: 0x2993
-  __TEXT.__objc_stubs: 0xdb00
+  __TEXT.__objc_stubs: 0xdb60
   __DATA_CONST.__got: 0x618
   __DATA_CONST.__const: 0x2178
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4158
+  __DATA_CONST.__objc_selrefs: 0x41a0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__auth_got: 0x520
   __AUTH_CONST.__const: 0x1340
   __AUTH_CONST.__cfstring: 0x6900
-  __AUTH_CONST.__objc_const: 0x117d8
+  __AUTH_CONST.__objc_const: 0x11860
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_ivar: 0x8c0
+  __DATA.__objc_ivar: 0x8c8
   __DATA.__data: 0xec0
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x19a0
   __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0x1b8
+  __DATA_DIRTY.__bss: 0x1a8
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C42E27C-2D71-3D3F-97A2-79F0D5FCD07E
-  Functions: 3607
-  Symbols:   11608
-  CStrings:  5726
+  UUID: BE016FC0-84E5-3D6C-ADBB-639B40B39AD9
+  Functions: 3618
+  Symbols:   11625
+  CStrings:  5744
 
Symbols:
+ +[BBSectionIconVariant variantWithFormat:dateComponentDetails:]
+ +[BBSectionIconVariant variantWithFormat:uti:]
+ -[BBObserver observerOptions]
+ -[BBObserver setObserverOptions:]
+ -[BBObserverClientProxy observerOptions]
+ -[BBObserverClientProxy setObserverOptions:]
+ -[BBObserverServerProxy setObserverOptions:]
+ -[BBSectionIconVariant dateComponentDetails]
+ -[BBSectionIconVariant setDateComponentDetails:]
+ -[BBSectionIconVariant setUti:]
+ -[BBSectionIconVariant uti]
+ GCC_except_table101
+ _OBJC_IVAR_$_BBObserver._observerOptions
+ _OBJC_IVAR_$_BBObserverClientProxy._observerOptions
+ ___55-[BBObserverServerProxy handleResponse:withCompletion:]_block_invoke.66
+ ___55-[BBObserverServerProxy handleResponse:withCompletion:]_block_invoke.67
+ ___72-[BBObserverServerProxy initWithObserver:connection:queue:calloutQueue:]_block_invoke.62
+ ___72-[BBObserverServerProxy initWithObserver:connection:queue:calloutQueue:]_block_invoke.63
+ ___block_literal_global.133
+ _objc_msgSend$decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:
+ _objc_msgSend$observerOptions
+ _objc_msgSend$setObserverOptions:
+ _xpcInterface.__interface.131
+ _xpcInterface.onceToken.130
- GCC_except_table44
- GCC_except_table97
- ___55-[BBObserverServerProxy handleResponse:withCompletion:]_block_invoke.64
- ___55-[BBObserverServerProxy handleResponse:withCompletion:]_block_invoke.65
- ___72-[BBObserverServerProxy initWithObserver:connection:queue:calloutQueue:]_block_invoke.60
- ___72-[BBObserverServerProxy initWithObserver:connection:queue:calloutQueue:]_block_invoke.61
- ___block_literal_global.131
- _xpcInterface.__interface.129
- _xpcInterface.onceToken.128
CStrings:
+ "%@ setObserverOptions: %@ options: %ld"
+ "%@ setObserverOptions: options: %ld"
+ "%{public}@ setObserverOptions: _connection: %{public}@ remoteObjectProxy: %{public}@"
+ "%{public}@ updateBulletin %{public}@ _connection: %@ remoteObjectProxy: %@"
+ "%{public}@ updateBulletin %{public}@ observer: %@"
+ "<%@ %p; feeds: %@; delegate: %@ observerOptions: %ld>"
+ "<%@: %p [%i:%@] observerOptions: %ld>"
+ "T@\"NSDictionary\",C,N"
+ "TQ,N,V_observerOptions"
+ "_observerOptions"
+ "_sendBulletinUpdate: FAILED to send to observer: %{public}@ typeDescription: %{public}@ %{public}@"
+ "_sendBulletinUpdate: observer: %{public}@ BBObserverOptionsObserveAll typeDescription: %{public}@ transactionID %ld %{public}@"
+ "_sendBulletinUpdate: observer: %{public}@ typeDescription: %{public}@ transactionID %ld, bulletin %{public}@"
+ "dateComponentDetails"
+ "decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:"
+ "observerOptions"
+ "setDateComponentDetails:"
+ "setObserverOptions:"
+ "setUti:"
+ "uti"
+ "variantWithFormat:dateComponentDetails:"
+ "variantWithFormat:uti:"
- "<%@ %p; feeds: %@; delegate: %@>"
- "<%@: %p [%@]>"
- "Can't send %{public}@ bulletin. No transactionID for bulletin %{public}@"
- "Sending %{public}@ bulletin with transactionID %ld, bulletin %{public}@"

```
