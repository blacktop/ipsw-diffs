## com.apple.iokit.IOVideoFamily

> `com.apple.iokit.IOVideoFamily`

```diff

-5590.80.3.0.0
+5590.100.8.0.0
   __TEXT.__cstring: 0x230
-  __TEXT_EXEC.__text: 0x48c4
+  __TEXT_EXEC.__text: 0x4978
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x2de0
   __DATA_CONST.__kalloc_type: 0x100
-  UUID: C002BC9A-96A7-369A-97D9-5036D6D9CE59
-  Functions: 265
-  Symbols:   711
+  UUID: B04067CF-C076-37F6-9CDA-16294E772E6B
+  Functions: 264
+  Symbols:   710
   CStrings:  35
 
Symbols:
- _ZN13IOVideoDevice24registerNotificationPortEP8ipc_portjj.cold.1
Functions:
~ __ZN13IOVideoDevice4freeEv : 128 -> 132
~ __ZN13IOVideoDevice13newUserClientEP4taskPvjP12OSDictionaryPP12IOUserClient : 632 -> 636
~ __ZN13IOVideoDevice24registerNotificationPortEP8ipc_portjj : 232 -> 240
~ __ZN13IOVideoDevice21sendMultiNotificationEjPK25IOVideoDeviceNotification : 292 -> 300
~ __Z27IOVideoDictionary_setUInt32P12OSDictionaryPKcj : 192 -> 208
~ __Z27IOVideoDictionary_setUInt64P12OSDictionaryPKcy : 192 -> 208
~ __ZN24IOVideoControlDictionary6createEjjjjjbjP8OSString : 420 -> 440
~ __ZN24IOVideoControlDictionary20createBooleanControlEjjjjjbbjP8OSString : 176 -> 196
~ __ZN24IOVideoControlDictionary13setIsReadOnlyEP12OSDictionaryb : 160 -> 176
~ __ZN24IOVideoControlDictionary22setBooleanControlValueEP12OSDictionaryb : 160 -> 176
~ __ZN27IOVideoDeviceUserClientInit27MergeDictionaryIntoProviderEP9IOServiceP12OSDictionary : 968 -> 992
~ __ZN23IOVideoDeviceUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 56 -> 76
~ __ZN23IOVideoStreamDictionary16setCurrentFormatEP12OSDictionaryRK24IOVideoStreamDescription : 176 -> 192
~ __ZN29IOVideoStreamFormatDictionary14getDescriptionEPK12OSDictionaryR24IOVideoStreamDescription : 116 -> 120

```
