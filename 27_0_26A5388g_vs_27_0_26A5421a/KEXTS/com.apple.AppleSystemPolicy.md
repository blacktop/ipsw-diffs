## com.apple.AppleSystemPolicy

> `com.apple.AppleSystemPolicy`

```diff

-823.0.3.0.0
+823.1.1.0.0
   __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x20ec
-  __TEXT.__os_log: 0x70b
-  __TEXT_EXEC.__text: 0xc330
-  __TEXT_EXEC.__auth_stubs: 0x990
+  __TEXT.__cstring: 0x22cb
+  __TEXT.__os_log: 0x790
+  __TEXT_EXEC.__text: 0xc764
+  __TEXT_EXEC.__auth_stubs: 0x9a0
   __DATA.__data: 0x858
   __DATA.__common: 0x1aa
   __DATA.__bss: 0x74

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x19e8
   __DATA_CONST.__kalloc_type: 0x180
-  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__auth_got: 0x4d0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x10
-  Functions: 295
-  Symbols:   920
-  CStrings:  273
+  Functions: 302
+  Symbols:   929
+  CStrings:  282
 
Symbols:
+ _ZN13ASPVnodeCache17setProvenanceDataEP5vnodeP18TrackingAttributes
+ _ZN13ASPVnodeCache18setLoggingCompleteEP5vnode
+ _ZN13ASPVnodeCache20clearLoggingCompleteEP5vnode
+ _ZN13ASPVnodeCache20setEvaluationResultsEP5vnodeP18evaluation_results
+ _ZN13ASPVnodeCache21setDeveloperToolStateEP5vnodei
+ _ZN13ASPVnodeCache23setEventPresentIfNeededEP5vnodehy
+ _ZN13ASPVnodeCache27checkAndSetTrackingUpcalledEP5vnode
+ __ZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfoPKc
+ __ZZ34asp_bastion_sandbox_event_callbackPKcP4procP5ucredE11_os_log_fmt_0
+ __ZZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfoPKcE11_os_log_fmt
+ __ZZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfoPKcE11_os_log_fmt_0
+ __ZZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfoPKcE11_os_log_fmt_1
+ _proc_best_name
- __ZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfo
- __ZZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfoE11_os_log_fmt
- __ZZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfoE11_os_log_fmt_0
- __ZZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfoE11_os_log_fmt_1
CStrings:
+ "\"ASPVnodeCache::checkAndSetTrackingUpcalled called with NULL vp\" @%s:%d"
+ "\"ASPVnodeCache::clearLoggingComplete called with NULL vp\" @%s:%d"
+ "\"ASPVnodeCache::setDeveloperToolState called with NULL vp\" @%s:%d"
+ "\"ASPVnodeCache::setEvaluationResults called with NULL vp\" @%s:%d"
+ "\"ASPVnodeCache::setEventPresentIfNeeded called with NULL vp\" @%s:%d"
+ "\"ASPVnodeCache::setLoggingComplete called with NULL vp\" @%s:%d"
+ "\"ASPVnodeCache::setProvenanceData called with NULL vp\" @%s:%d"
+ "ASPVnodeCache.cpp"
+ "Skipping ASP sandbox event evaluation: responsible process (pid %d, name %s) has no executable vnode (rule %s, proc pid %d, name %s)"
```
