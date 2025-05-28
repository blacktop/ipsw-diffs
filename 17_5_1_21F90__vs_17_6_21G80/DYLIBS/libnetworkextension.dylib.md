## libnetworkextension.dylib

> `/usr/lib/libnetworkextension.dylib`

```diff

-1838.122.1.0.0
-  __TEXT.__text: 0x2bd90
+1838.140.5.0.1
+  __TEXT.__text: 0x2cd10
   __TEXT.__auth_stubs: 0x1790
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x24d9
-  __TEXT.__oslogstring: 0x6798
-  __TEXT.__unwind_info: 0x650
+  __TEXT.__cstring: 0x24e1
+  __TEXT.__oslogstring: 0x6f8e
+  __TEXT.__unwind_info: 0x658
   __TEXT.__objc_classname: 0x13
   __TEXT.__objc_methname: 0x11b
   __TEXT.__objc_methtype: 0x11

   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0xbd0
   __AUTH.__objc_data: 0x50
-  __DATA.__data: 0x744
+  __DATA.__data: 0x53c
   __DATA.__common: 0x3d
-  __DATA.__bss: 0x388
+  __DATA.__bss: 0x588
   __DATA_DIRTY.__const: 0xe0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x300

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 523
-  Symbols:   1442
-  CStrings:  874
+  Functions: 525
+  Symbols:   1444
+  CStrings:  882
 
Symbols:
+ _NEHelperTrackerAddIPForAllFlowsRedactLogs
+ _NEHelperTrackerAddIPForAllFlowsRedactLogs.buffer
+ _NEHelperTrackerGetDispositionRedactLogs
+ _NEHelperTrackerGetDispositionRedactLogs.buffer
+ ___block_descriptor_tmp.12.421
+ ___block_descriptor_tmp.13.422
+ ___block_descriptor_tmp.13.531
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.159.293
+ ___block_descriptor_tmp.160.294
+ ___block_descriptor_tmp.177.114
+ ___block_descriptor_tmp.18.432
+ ___block_descriptor_tmp.19.433
+ ___block_descriptor_tmp.190.162
+ ___block_descriptor_tmp.196.173
+ ___block_descriptor_tmp.20.384
+ ___block_descriptor_tmp.20.434
+ ___block_descriptor_tmp.30.390
+ ___block_descriptor_tmp.313
+ ___block_descriptor_tmp.35.466
+ ___block_descriptor_tmp.375
+ ___block_descriptor_tmp.41.442
+ ___block_descriptor_tmp.427
+ ___block_descriptor_tmp.46.520
+ ___block_descriptor_tmp.47.510
+ ___block_descriptor_tmp.48.487
+ ___block_literal_global.131
+ ___block_literal_global.311
+ ___block_literal_global.377
+ ___block_literal_global.425
+ _ne_session_trim_domain.domain_buffer.221
- _NEHelperTrackerAddIPForAllFlows.buffer
- _NEHelperTrackerGetDisposition.buffer
- ___block_descriptor_tmp.12.412
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.13.413
- ___block_descriptor_tmp.13.522
- ___block_descriptor_tmp.159.284
- ___block_descriptor_tmp.160.285
- ___block_descriptor_tmp.177.105
- ___block_descriptor_tmp.18.423
- ___block_descriptor_tmp.19.424
- ___block_descriptor_tmp.190.153
- ___block_descriptor_tmp.196.164
- ___block_descriptor_tmp.20.375
- ___block_descriptor_tmp.20.425
- ___block_descriptor_tmp.30.381
- ___block_descriptor_tmp.304
- ___block_descriptor_tmp.35.457
- ___block_descriptor_tmp.366
- ___block_descriptor_tmp.41.433
- ___block_descriptor_tmp.418
- ___block_descriptor_tmp.46.511
- ___block_descriptor_tmp.47.501
- ___block_descriptor_tmp.48.478
- ___block_literal_global.122
- ___block_literal_global.302
- ___block_literal_global.368
- ___block_literal_global.416
- _ne_session_trim_domain.domain_buffer.212
CStrings:
+ "%s Invalid app info for domain%{sensitive, mask.hash, networkextension:string}.*P (app info ref %X pid %d for %s) %s - %s"
+ "%s Invalid domain length%{sensitive, mask.hash, networkextension:string}.*P (app info ref %X pid %d for %s) %s - %s"
+ "%s domain lookup for puny-coded%{sensitive, mask.hash, networkextension:string}.*P (app info ref %X pid %d for %s) %s - %s"
+ "%s domain lookup for%{sensitive, mask.hash, networkextension:string}.*P (app info ref %X pid %d for %s) %s - %s"
+ "%s: Invalid app info for domain<%d : %{private}s> (app info ref %X pid %d for %s) %s - %s"
+ "%s: Invalid domain length<%d : %{private}s> (app info ref %X pid %d for %s) %s - %s"
+ "%s: completed for%{sensitive, mask.hash, networkextension:string}.*P %{sensitive, mask.hash, networkextension:string}.*P app <%d : %s> %{sensitive, mask.hash, networkextension:string}.*P <app approved %d> <is_tracker %d> (error = %d)"
+ "%s: completed for<%d : %{private}s> <%d : %{private}s> app <%d : %s> <%d : %{private}s> <app approved %d> <is_tracker %d> (error = %d)"
+ "%s: domain lookup - found match for tracker domain (pid %d %s)%s for %s"
+ "%s: domain lookup - found match for tracker%{sensitive, mask.hash, networkextension:string}.*P --> metadata %{sensitive, mask.hash, networkextension:string}.*P %{sensitive, mask.hash, networkextension:string}.*P (app info ref %X pid %d %s) %s - %s"
+ "%s: domain lookup - found match for tracker<%d : %{private}s> --> metadata <%d : %{private}s> <%d : %{private}s> (app info ref %X pid %d %s) %s - %s"
+ "%s: domain lookup for puny-coded<%d : %{private}s> (app info ref %X pid %d for %s) %s - %s"
+ "%s: domain lookup for<%d : %{private}s> (app info ref %X pid %d for %s) %s - %s"
+ "%s: domain lookup result for puny-coded%{sensitive, mask.hash, networkextension:string}.*P --> metadata %{sensitive, mask.hash, networkextension:string}.*P %{sensitive, mask.hash, networkextension:string}.*P (app info ref %X pid %d %s) %s - %s"
+ "%s: domain lookup result for puny-coded<%d : %{private}s> --> metadata <%d : %{private}s> <%d : %{private}s> (app info ref %X pid %d %s) %s - %s"
+ "%s: domain lookup result for%{sensitive, mask.hash, networkextension:string}.*P --> metadata %{sensitive, mask.hash, networkextension:string}.*P %{sensitive, mask.hash, networkextension:string}.*P (app info ref %X pid %d %s) %s - %s"
+ "%s: domain lookup result for<%d : %{private}s> --> metadata <%d : %{private}s> <%d : %{private}s> (app info ref %X pid %d %s) %s - %s"
+ "%s: failed for%{sensitive, mask.hash, networkextension:string}.*P %{sensitive, mask.hash, networkextension:string}.*P app <%d : %s> %{sensitive, mask.hash, networkextension:string}.*P <app approved %d> <is_tracker %d> (error = %d)"
+ "%s: failed for<%d : %{private}s> <%d : %{private}s> app <%d : %s> <%d : %{private}s> <app approved %d> <is_tracker %d> (error = %d)"
+ "NEHelperTrackerAddIPForAllFlowsRedactLogs"
+ "n/a"
- "%s: Invalid app info for domain %s (app info ref %X pid %d)"
- "%s: Invalid domain %s (app info ref %X pid %d)"
- "%s: NEHelperTrackerGetDispositionForDomain for domain %s (app info ref %X pid %d)"
- "%s: completed for <%s> owner <%s> app <%d : %s> <%s> <app approved %d> <is_tracker %d>"
- "%s: domain lookup result for <%s> --> metadata <%s> <%s> (app info ref %X pid %d)"
- "%s: failed for <%s> owner <%s> app <%d : %s> <%s> <app approved %d> <is_tracker %d> (error = %d)"
- "%s: found match for domain <%s> metadata <%s> <%s> (app info ref %X pid %d %s)%s for %s"
- "%s: found match for tracker domain (pid %d %s)%s for %s"
- "%s: lookup for <%s> length %d (app info ref %X pid %d for %s)"
- "%s: lookup for puny-coded <%s> length %d"
- "<nil>"
- "NEHelperTrackerAddIPForAllFlows"
- "Puny-coding domain <%s> for socket"

```
