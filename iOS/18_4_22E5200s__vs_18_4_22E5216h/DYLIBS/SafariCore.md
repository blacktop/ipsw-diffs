## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-621.1.10.20.6
-  __TEXT.__text: 0xf61b0
-  __TEXT.__auth_stubs: 0x2740
-  __TEXT.__objc_methlist: 0xa8a4
-  __TEXT.__const: 0x16e8
-  __TEXT.__gcc_except_tab: 0x62bc
-  __TEXT.__cstring: 0x107a5
+621.1.13.10.4
+  __TEXT.__text: 0xfae44
+  __TEXT.__auth_stubs: 0x2760
+  __TEXT.__objc_methlist: 0xa944
+  __TEXT.__const: 0x16f8
+  __TEXT.__gcc_except_tab: 0x637c
+  __TEXT.__cstring: 0x10955
   __TEXT.__ustring: 0x2748
-  __TEXT.__oslogstring: 0x96fa
+  __TEXT.__oslogstring: 0x987a
   __TEXT.__dlopen_cstrs: 0x19b
-  __TEXT.__swift5_typeref: 0x8d1
+  __TEXT.__swift5_typeref: 0x90b
   __TEXT.__swift5_fieldmd: 0x4a4
   __TEXT.__constg_swiftt: 0x490
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x74
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__swift_as_entry: 0x8c
+  __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x5508
-  __TEXT.__eh_frame: 0x1c68
+  __TEXT.__unwind_info: 0x55a0
+  __TEXT.__eh_frame: 0x1da8
   __TEXT.__objc_classname: 0x1864
-  __TEXT.__objc_methname: 0x21711
+  __TEXT.__objc_methname: 0x218f4
   __TEXT.__objc_methtype: 0x3b9b
-  __TEXT.__objc_stubs: 0x10780
-  __DATA_CONST.__got: 0xc48
-  __DATA_CONST.__const: 0x4a90
+  __TEXT.__objc_stubs: 0x108c0
+  __DATA_CONST.__got: 0xcc0
+  __DATA_CONST.__const: 0x4b58
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x150
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62d8
+  __DATA_CONST.__objc_selrefs: 0x6340
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x438
-  __DATA_CONST.__objc_arraydata: 0x2720
-  __AUTH_CONST.__auth_got: 0x13b8
-  __AUTH_CONST.__auth_ptr: 0x390
-  __AUTH_CONST.__const: 0x3d80
-  __AUTH_CONST.__cfstring: 0x17a00
-  __AUTH_CONST.__objc_const: 0x110b0
+  __DATA_CONST.__objc_arraydata: 0x2740
+  __AUTH_CONST.__auth_got: 0x13c8
+  __AUTH_CONST.__auth_ptr: 0x310
+  __AUTH_CONST.__const: 0x3e30
+  __AUTH_CONST.__cfstring: 0x17ae0
+  __AUTH_CONST.__objc_const: 0x11110
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH_CONST.__objc_arrayobj: 0x558
+  __AUTH_CONST.__objc_arrayobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xb28
   __AUTH.__data: 0x318
-  __DATA.__objc_ivar: 0xad4
-  __DATA.__data: 0x14f0
+  __DATA.__objc_ivar: 0xad8
+  __DATA.__data: 0x1510
   __DATA.__bss: 0x2400
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x2b48

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5913
-  Symbols:   6471
-  CStrings:  8897
+  Functions: 5951
+  Symbols:   6502
+  CStrings:  8931
 
Symbols:
+ __ZN12SafariShared25SuddenTerminationDisablerC1EP8NSStringU13block_pointerFvvE
+ __ZN12SafariShared25SuddenTerminationDisablerC2EP8NSStringU13block_pointerFvvE
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
- _xmlFree
CStrings:
+ "+[NSBundle(SafariCoreExtras) safari_safariServicesInjectedBundleURL]"
+ "@\"NSDate\"24@?0@\"<WBSSavedAccountSidecarInternal>\"8@\"NSDate\"16"
+ "@\"NSDate\"24@?0@\"NSDate\"8@\"NSDate\"16"
+ "@\"NSDate\"24@?0@\"WBSSavedAccountSidecarContextSpecificData\"8@\"NSDate\"16"
+ "@\"NSDate\"32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "@\"NSNumber\"32@?0@\"NSString\"8@\"NSDate\"16^B24"
+ "Background Task Expired. %@, database URL: %@"
+ "Cancelled replacing file because Destination path is empty."
+ "Failed to replace the file at (%{public}@). Error: %{public}@"
+ "File to replace still exist after removal at %{public}@. Error: %{public}@"
+ "Found %ld accounts with matching user for domain %{sensitive}s"
+ "Origin file is not readable %{public}@. Cancelling replacement of %{public}@."
+ "SafariServices.framework"
+ "SafariServices.wkbundle"
+ "TB,R,N,V_safariIsTerminating"
+ "_siteIsAdditionalSite:"
+ "_sitesToLastUsedDates"
+ "chatgpt"
+ "com.apple.JavaScriptCore"
+ "copyItemAtURL:toURL:error:"
+ "deleteTabGroupEntitiesWithUUIDStrings:completionHandler:"
+ "hasProtectionSpaceForAdditionalSite:"
+ "isReadableFileAtPath:"
+ "lastUsedDateAcrossAllContextsAndSites"
+ "lastUsedDateAcrossAllContextsForSite:"
+ "lastUsedDateAcrossAllSites"
+ "lastUsedDateForSite:"
+ "lastUsedDateForSite:inContext:"
+ "openai"
+ "removeLastUsedDateForSite:"
+ "safariIsTerminating"
+ "safari_replaceItemAtURL:withItemFromURL:error:"
+ "safari_safariServicesInjectedBundleURL"
+ "setLastUsedDate:forSite:"
+ "setLastUsedDate:forSite:inContext:"
+ "slUsed"
+ "sora"
- "lastUsedDateAcrossAllContexts"
- "lastUsedDateForContext:"
- "setLastUsedDate:forContext:"

```
