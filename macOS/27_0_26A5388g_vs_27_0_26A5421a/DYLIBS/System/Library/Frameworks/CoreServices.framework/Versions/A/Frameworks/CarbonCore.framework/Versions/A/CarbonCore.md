## CarbonCore

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/CarbonCore.framework/Versions/A/CarbonCore`

```diff

-1405.0.0.0.0
-  __TEXT.__text: 0xedb58
+1406.0.0.0.0
+  __TEXT.__text: 0xeb534
   __TEXT.__objc_methlist: 0x68
-  __TEXT.__const: 0x1cdd60
-  __TEXT.__cstring: 0x2ab67
-  __TEXT.__oslogstring: 0x7ff0
-  __TEXT.__gcc_except_tab: 0x760
-  __TEXT.__unwind_info: 0x3988
+  __TEXT.__const: 0x1cdd18
+  __TEXT.__cstring: 0x2a9ba
+  __TEXT.__oslogstring: 0x7d80
+  __TEXT.__gcc_except_tab: 0x758
+  __TEXT.__unwind_info: 0x3948
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15460
+  __DATA_CONST.__const: 0x153f0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3bf8
-  __AUTH_CONST.__cfstring: 0x4ae0
+  __AUTH_CONST.__const: 0x3ae8
+  __AUTH_CONST.__cfstring: 0x4a60
   __AUTH_CONST.__objc_const: 0x40
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x1aa0
+  __AUTH_CONST.__auth_got: 0x1a98
   __AUTH.__data: 0x5a8
   __DATA.__data: 0x1308
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x340
-  __DATA.__bss: 0x50d8
+  __DATA.__bss: 0x50c0
   __DATA_DIRTY.__data: 0x440
   __DATA_DIRTY.__bss: 0x690
   __DATA_DIRTY.__common: 0x14

   - /usr/lib/libfakelink.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5094
-  Symbols:   7109
-  CStrings:  6890
+  Functions: 5053
+  Symbols:   7063
+  CStrings:  6858
 
Symbols:
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table63
- GCC_except_table56
- GCC_except_table62
- GCC_except_table72
- __XCacheableSetWithStringKey
- __XPrefsForgetKey
- __XPrefsGetInteger
- __XPrefsGetString
- __XPrefsPostData
- __XPrefsSetInteger
- __XPrefsSetString
- __ZL9_addValuePKvS0_Pv
- __ZN11SCCacheable16SetWithStringKeyEjPKcmj
- __ZN11SCCacheable16SetWithStringKeyEjPKcmj13audit_token_t
- __ZN15RemoteCacheable16SetWithStringKeyEjPKcmj
- __ZN15SCClientSession10getIntegerEPKcPi
- __ZN15SCClientSession10setIntegerEPKci
- __ZN15SCClientSession7addDataEPKvl
- __ZN15SCClientSession8flushKeyEPKc
- __ZN15SCClientSession9getStringEPKcPc
- __ZN15SCClientSession9setStringEPKcS1_
- __ZN9SCSession10addToPrefsERK11PrefsBucket
- __ZN9SCSession10getIntegerEPKcPi
- __ZN9SCSession10setIntegerEPKci
- __ZN9SCSession14getPrefsBucketEPKc
- __ZN9SCSession7addDataEPKvl
- __ZN9SCSession8flushKeyEPKc
- __ZN9SCSession9getStringEPKcPc
- __ZN9SCSession9setStringEPKcS1_
- __ZNSt3__119__allocate_at_leastB9nqe220106INS_9allocatorI11PrefsBucketEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
- __ZNSt3__16vectorI11PrefsBucketNS_9allocatorIS1_EEE20__throw_length_errorB9nqe220106Ev
- __ZNSt3__16vectorI11PrefsBucketNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
- __ZZL9_addValuePKvS0_PvE10sBooleanID
- __ZZL9_addValuePKvS0_PvE9sNumberID
- __ZZL9_addValuePKvS0_PvE9sStringID
- __scsclient_CacheableSetWithStringKey
- __scsclient_PrefsForgetKey
- __scsclient_PrefsGetInteger
- __scsclient_PrefsGetString
- __scsclient_PrefsPostData
- __scsclient_PrefsSetInteger
- __scsclient_PrefsSetString
- __scsserver_CacheableSetWithStringKey
- __scsserver_PrefsForgetKey
- __scsserver_PrefsGetInteger
- __scsserver_PrefsGetString
- __scsserver_PrefsPostData
- __scsserver_PrefsSetInteger
- __scsserver_PrefsSetString
- _sandbox_check_by_audit_token
CStrings:
- "    %d: %s"
- " - int value %d (0x%x)\n"
- " - str value '%s'\n"
- "%s: Adding pref int for key %s, value %d"
- "%s: Adding pref string for key %s, value %s"
- "%s: Looking for pref: %s"
- "%s: NAMEDDATA: deallocating passed in data, %p/%d, because the client %d is sandboxed or no cacheable exists"
- "%s: forgetKey:session=%{public}p uid=%{public}d %{public}s"
- "%s: getInteger:session=%{public}p uid=%{public}d %{public}s"
- "%s: getString:session=%{public}p uid=%{public}d %{public}s"
- "%s: not found!"
- "%s: postData:session=%{public}p uid=%{public}d %{public}p,%{public}d"
- "%s: setInteger:session=%{public}p uid=%{public}d %{public}s=%{public}d"
- "%s: setString:session=%{public}p uid=%{public}d %{public}s=>%{private}s"
- "CacheableSetWithStringKey"
- "Has prefs: %d slots\n"
- "PrefsForgetKey"
- "PrefsGetInteger"
- "PrefsGetString"
- "PrefsPostData"
- "PrefsSetInteger"
- "PrefsSetString"
- "SetWithStringKey"
- "_scsserver_CacheableSetWithStringKey"
- "_scsserver_PrefsForgetKey"
- "_scsserver_PrefsGetInteger"
- "_scsserver_PrefsGetString"
- "_scsserver_PrefsPostData"
- "_scsserver_PrefsSetInteger"
- "_scsserver_PrefsSetString"
- "addToPrefs"
- "getPrefsBucket"
```
