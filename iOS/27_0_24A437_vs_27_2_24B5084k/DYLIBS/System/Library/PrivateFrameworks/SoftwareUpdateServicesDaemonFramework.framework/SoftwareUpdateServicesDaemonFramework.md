## SoftwareUpdateServicesDaemonFramework

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesDaemonFramework.framework/SoftwareUpdateServicesDaemonFramework`

```diff

-1112.0.3.0.0
-  __TEXT.__text: 0x60880
-  __TEXT.__objc_methlist: 0x51a4
+1114.40.9.0.0
+  __TEXT.__text: 0x60d38
+  __TEXT.__objc_methlist: 0x51e4
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x110f8
+  __TEXT.__cstring: 0x111d1
   __TEXT.__oslogstring: 0x852
-  __TEXT.__gcc_except_tab: 0x7a8
-  __TEXT.__unwind_info: 0x20f0
+  __TEXT.__gcc_except_tab: 0x79c
+  __TEXT.__unwind_info: 0x2108
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e38
+  __DATA_CONST.__objc_selrefs: 0x3e68
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__got: 0xad0
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x8c80
-  __AUTH_CONST.__objc_const: 0x83d0
+  __AUTH_CONST.__cfstring: 0x8d40
+  __AUTH_CONST.__objc_const: 0x8400
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x508
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x354
+  __DATA.__objc_ivar: 0x358
   __DATA.__data: 0x840
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__bss: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2142
-  Symbols:   5234
-  CStrings:  1507
+  Functions: 2149
+  Symbols:   5248
+  CStrings:  1514
 
Symbols:
+ -[SUAutoInstallManager _queue_scheduleAutoUpdateBannerIfNeededForReason:]
+ -[SUPolicyFactory _resolvedPersonalizationServerURL]
+ -[SUPolicyFactory personalizationServerURL]
+ -[SUPolicyFactory setPersonalizationServerURL:]
+ -[SUScanner _shouldRescanForScanOptions:previousScanError:hasDoneSplatScan:reason:]
+ GCC_except_table90
+ _OBJC_IVAR_$_SUPolicyFactory._personalizationServerURL
+ ___43-[SUPolicyFactory personalizationServerURL]_block_invoke
+ ___47-[SUPolicyFactory setPersonalizationServerURL:]_block_invoke
+ _objc_msgSend$_queue_scheduleAutoUpdateBannerIfNeededForReason:
+ _objc_msgSend$_resolvedPersonalizationServerURL
+ _objc_msgSend$_shouldRescanForScanOptions:previousScanError:hasDoneSplatScan:reason:
+ _objc_msgSend$overridePersonalizationURL
+ _objc_msgSend$personalizationServerURL
+ _objc_msgSend$setPersonalizationServerURL:
- GCC_except_table89
CStrings:
+ "\t"
+ "%@: install tonight is scheduled and download is done. Displaying banner"
+ "%@: no passcode set. Displaying banner"
+ "%s - will rescan for updates, reason = '%@', with options %@"
+ "%s: T&Cs already accepted"
+ "Auto update consented"
+ "Not performing space check for updatesDownloadable since there is an in-progress/finished download"
+ "Operation auto-consented"
+ "Overriding Tatsu personalization server URL for this update: %@"
+ "Will not rescan for Splat -- disabled by Preferences"
+ "Will not rescan for updates"
+ "Will rescan for Splat updates"
+ "[DDM] Fall back to a scan for Splat updates"
+ "[DDM] Fall back to a scan for regular updates"
- "%s - [DDM] Fall back to a scan for Splat updates"
- "%s - [DDM] Fall back to a scan for regular updates"
- "%s - will not rescan for Splat -- disabled by default"
- "%s - will rescan for updates with options %@"
- "Auto update consented and no passcode set. Displaying banner"
- "Install tonight is scheduled and download is done. Displaying banner"
- "Not performing space check since there is an in-progress download"
```
