## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-370.38.2.0.0
-  __TEXT.__text: 0x1e677c
+370.40.2.0.0
+  __TEXT.__text: 0x1e71b0
   __TEXT.__auth_stubs: 0x1860
-  __TEXT.__delay_stubs: 0x500
-  __TEXT.__delay_helper: 0x16f4
-  __TEXT.__objc_stubs: 0xdf20
-  __TEXT.__objc_methlist: 0x9d6c
+  __TEXT.__delay_stubs: 0x540
+  __TEXT.__delay_helper: 0x172c
+  __TEXT.__objc_stubs: 0xdf40
+  __TEXT.__objc_methlist: 0x9d9c
   __TEXT.__const: 0x144c
-  __TEXT.__cstring: 0x226d3
-  __TEXT.__oslogstring: 0x2038d
+  __TEXT.__cstring: 0x22880
+  __TEXT.__oslogstring: 0x205b3
   __TEXT.__objc_classname: 0x1d44
-  __TEXT.__objc_methname: 0x1585d
-  __TEXT.__objc_methtype: 0x4dfe
-  __TEXT.__unwind_info: 0x2c50
-  __DATA_CONST.__const: 0x9a00
-  __DATA_CONST.__cfstring: 0x112a0
+  __TEXT.__objc_methname: 0x158cd
+  __TEXT.__objc_methtype: 0x4e1f
+  __TEXT.__unwind_info: 0x2c48
+  __DATA_CONST.__const: 0x9a50
+  __DATA_CONST.__cfstring: 0x11320
   __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x388

   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_intobj: 0x7bf0
-  __DATA_CONST.__objc_arraydata: 0x1e38
-  __DATA_CONST.__objc_dictobj: 0x1018
+  __DATA_CONST.__objc_arraydata: 0x1e58
+  __DATA_CONST.__objc_dictobj: 0x1040
   __DATA_CONST.__objc_arrayobj: 0x318
-  __DATA_CONST.__auth_got: 0xcd8
-  __DATA_CONST.__got: 0x9f8
+  __DATA_CONST.__auth_got: 0xce0
+  __DATA_CONST.__got: 0xa00
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x14e48
-  __DATA.__objc_selrefs: 0x4b60
-  __DATA.__objc_ivar: 0x112c
+  __DATA.__objc_const: 0x14ea8
+  __DATA.__objc_selrefs: 0x4b78
+  __DATA.__objc_ivar: 0x1134
   __DATA.__objc_data: 0x3f20
   __DATA.__data: 0x2b34
   __DATA.__bss: 0x2c0

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4269
-  Symbols:   669
-  CStrings:  11365
+  Functions: 4274
+  Symbols:   671
+  CStrings:  11389
 
Symbols:
+ _ACMContextGetExternalForm
+ _OBJC_CLASS_$_SECPresentmentAuthorizationStore
CStrings:
+ "%@ { applet=%@ endpoint=%@ didError=%@ result=%@ brandCode=%@ background=%@ }"
+ "%{public}s:%i Context & credential binding failed, status=%d"
+ "%{public}s:%i Context creation failed, status=%d"
+ "%{public}s:%i Credential creation failed, status=%d"
+ "%{public}s:%i Invalid NLEN value; 0xFFFF is RFU"
+ "%{public}s:%i NDEF message is larger than storage (%lu bytes)"
+ "%{public}s:%i NLEN=%d exceeds NDEF capacity (%lu bytes); rejecting out-of-bounds message"
+ "%{public}s:%i Stash presentment auth error, %{public}@"
+ "%{public}s:%i Touch system ready event expired"
+ "%{public}s:%i Touch system ready event expired, last systemAvailable=%d"
+ "%{public}s:%i Unexpected context"
+ "%{public}s:%i Unexpected state; workQueue is nil"
+ "-[NFBackgroundTagReadingManager initWithQueue:driverWrapper:]_block_invoke_2"
+ "-[NFTNEPHandler _updateTagMemoryWithNDEF:]"
+ "-[NFWalletPresentationEventPublisher _createButtonPressedACMRef]"
+ "-[NFWalletPresentationEventPublisher _createButtonPressedACMRef]_block_invoke"
+ "@\"NSMutableDictionary\"8@?0"
+ "Invalid NLEN detected"
+ "NFCD built from (B&I) Stockholm_Base-370.40.2"
+ "TNEP reader writes an invalid NDEF message; abort transaction attempt"
+ "Vv24@0:8@?<v@?@\"NSDictionary\">16"
+ "_assertionHeld"
+ "currentDeviceCAParametersWithCompletion:"
+ "disableFuryStandby"
+ "endSessionWithReason:completion:"
+ "localDeviceCAParameters"
+ "stashPresentmentAuthExternalForm:bundleID:error:"
+ "v24@?0r^v8Q16"
- "%@ { applet=%@ endpoint=%@ didError=%@ result=%@ brandCode=%@ }"
- "%{public}s:%i Touch system ready event expired, systemAvailable=%d"
- "NFCD built from (B&I) Stockholm_Base-370.38.2"
- "unarchivedArrayOfObjectsOfClasses:fromData:error:"
```
