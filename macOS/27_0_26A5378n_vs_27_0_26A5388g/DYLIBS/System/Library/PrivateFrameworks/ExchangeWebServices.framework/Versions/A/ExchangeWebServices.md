## ExchangeWebServices

> `/System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-842.0.0.0.0
-  __TEXT.__text: 0x39034
-  __TEXT.__objc_methlist: 0xa580
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xa09a
-  __TEXT.__oslogstring: 0xb29
-  __TEXT.__gcc_except_tab: 0x558
-  __TEXT.__unwind_info: 0x1070
+844.0.0.0.0
+  __TEXT.__text: 0x3a050
+  __TEXT.__objc_methlist: 0xa600
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0xa103
+  __TEXT.__oslogstring: 0xd8f
+  __TEXT.__gcc_except_tab: 0x56c
+  __TEXT.__unwind_info: 0x10a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3840
+  __DATA_CONST.__objc_selrefs: 0x3898
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0xff8
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0xfe00
-  __AUTH_CONST.__objc_const: 0x48fc8
+  __DATA_CONST.__got: 0x1000
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0xfe80
+  __AUTH_CONST.__objc_const: 0x49070
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH.__objc_data: 0x9650
-  __DATA.__objc_ivar: 0xf40
+  __DATA.__objc_ivar: 0xf50
   __DATA.__data: 0x548
-  __DATA.__bss: 0x1a8
+  __DATA.__bss: 0x1c8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2988
-  Symbols:   8381
-  CStrings:  2131
+  Functions: 3007
+  Symbols:   8415
+  CStrings:  2141
 
Symbols:
+ +[EWSExchangeServiceBinding _errorIsCapInducedTimedOut:]
+ +[EWSExchangeServiceBinding _errorIsConnectTimeoutETIMEDOUT:]
+ +[EWSExchangeServiceBinding _internalURLHasFreshConnectTimeoutForAccountIdentifier:internalURL:externalURL:]
+ +[EWSExchangeServiceBinding _preferredURLForAccountIdentifier:internalURL:externalURL:]
+ +[EWSExchangeServiceBinding _recordURLPreferenceFailureForAccountIdentifier:internalURL:externalURL:atDate:]
+ +[EWSExchangeServiceBinding _resetURLPreferenceCacheForTests]
+ +[EWSExchangeServiceBinding _urlPreferenceCacheKeyForAccountIdentifier:internalURL:externalURL:]
+ +[EWSExchangeServiceBindingTask log]
+ -[EWSExchangeServiceBindingTask eligibleForFirstProbeCap]
+ -[EWSExchangeServiceBindingTask setEligibleForFirstProbeCap:]
+ GCC_except_table29
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table52
+ OBJC_IVAR_$_EWSExchangeServiceBinding._capIssuedTasks
+ OBJC_IVAR_$_EWSExchangeServiceBinding._hasIssuedFirstProbe
+ OBJC_IVAR_$_EWSExchangeServiceBinding._hasURLFallback
+ OBJC_IVAR_$_EWSExchangeServiceBindingTask._eligibleForFirstProbeCap
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSCache
+ __OBJC_$_CLASS_METHODS_EWSExchangeServiceBindingTask
+ __OBJC_$_CLASS_PROP_LIST_EWSExchangeServiceBindingTask
+ ___36+[EWSExchangeServiceBindingTask log]_block_invoke
+ ___39+[EWSExchangeServiceBinding initialize]_block_invoke
+ _gURLPreferenceCache
+ _objc_msgSend$_errorIsCapInducedTimedOut:
+ _objc_msgSend$_errorIsConnectTimeoutETIMEDOUT:
+ _objc_msgSend$_internalURLHasFreshConnectTimeoutForAccountIdentifier:internalURL:externalURL:
+ _objc_msgSend$_preferredURLForAccountIdentifier:internalURL:externalURL:
+ _objc_msgSend$_recordURLPreferenceFailureForAccountIdentifier:internalURL:externalURL:atDate:
+ _objc_msgSend$_urlPreferenceCacheKeyForAccountIdentifier:internalURL:externalURL:
+ _objc_msgSend$eligibleForFirstProbeCap
+ _objc_msgSend$identifier
+ _objc_msgSend$lockWhenCondition:beforeDate:
+ _objc_msgSend$setCountLimit:
+ _objc_msgSend$setEligibleForFirstProbeCap:
+ _objc_msgSend$setName:
+ initialize.onceToken
+ log.once
- GCC_except_table21
- GCC_except_table22
- GCC_except_table23
- GCC_except_table24
- GCC_except_table33
- GCC_except_table34
- GCC_except_table36
- GCC_except_table43
- _objc_msgSend$lockWhenCondition:
CStrings:
+ "%{public}@ EWS request timed out after %{public}.1f seconds AND post-cancel wait exceeded its 5s safety bound; URLSession delegate queue may be wedged (request: %{public}@, clientRequestID: %{public}@). rdar://176555434 — fabricated NSURLErrorTimedOut."
+ "%{public}@ EWS request timed out after %{public}.1f seconds; cancellation drove cleanup (request: %{public}@, clientRequestID: %{public}@). rdar://176555434 — guard fired."
+ "(none)"
+ "EWSURLPreferenceCache"
+ "ExchangeServiceBindingTask"
+ "URL preference cache: recorded internal connect-timeout failure for account %{public}@."
+ "URL preference cache: swapping internal->external for account %{public}@ (fresh failure marker)."
+ "_kCFStreamErrorCodeKey"
+ "_kCFStreamErrorDomainKey"
+ "\xf01"
```
