## DesktopServicesPriv

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv`

```diff

-1857.0.0.0.0
-  __TEXT.__text: 0x227d3c
-  __TEXT.__objc_methlist: 0x3d74
-  __TEXT.__gcc_except_tab: 0x34ca4
+1857.1.4.0.0
+  __TEXT.__text: 0x228294
+  __TEXT.__objc_methlist: 0x3dbc
+  __TEXT.__gcc_except_tab: 0x34d0c
   __TEXT.__const: 0x83a0
   __TEXT.__cstring: 0x9f4e
-  __TEXT.__oslogstring: 0x86d1
+  __TEXT.__oslogstring: 0x874a
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x11440
+  __TEXT.__unwind_info: 0x11450
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xd70
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0x2680

   __DATA_CONST.__got: 0xcc8
   __AUTH_CONST.__const: 0xb608
   __AUTH_CONST.__cfstring: 0x4a60
-  __AUTH_CONST.__objc_const: 0x6408
+  __AUTH_CONST.__objc_const: 0x6418
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH.__objc_data: 0x11d0
   __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x314
-  __DATA.__data: 0x898
+  __DATA.__data: 0x8f8
   __DATA.__common: 0xe1
   __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__data: 0x4d8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libfakelink.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9824
-  Symbols:   16772
-  CStrings:  2365
+  Functions: 9828
+  Symbols:   16780
+  CStrings:  2367
 
Symbols:
+ -[FIChildrenIterator countByEnumeratingWithState:objects:count:]
+ -[FICompoundNodeIterator countByEnumeratingWithState:objects:count:]
+ -[FINodeIterator countByEnumeratingWithState:objects:count:]
+ -[FINodeIteratorWithExtraChildren countByEnumeratingWithState:objects:count:]
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFastEnumeration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFastEnumeration
+ __OBJC_LABEL_PROTOCOL_$_NSFastEnumeration
+ __OBJC_PROTOCOL_$_NSFastEnumeration
+ __ZN13TNodeIterator27CountByEnumeratingWithStateER22NSFastEnumerationStateNSt3__14spanIP11objc_objectLm18446744073709551615EEE
- __Z20IsDomainDisconnectedP16FPProviderDomain
Functions:
+ __ZN13TNodeIterator27CountByEnumeratingWithStateER22NSFastEnumerationStateNSt3__14spanIP11objc_objectLm18446744073709551615EEE
~ __ZN10TOperation16ProcessSelectionEv : 408 -> 572
~ __DesktopServicesErrorName : 12 -> 4
- __Z20IsDomainDisconnectedP16FPProviderDomain
~ -[FINode fiTags] : 612 -> 628
- __ZN23FIProviderDomainFetcherC2Ev
~ __ZN23FIProviderDomainFetcher16FetchDomainForIDEP8NSString27FPProviderDomainCachePolicyP5NSURLPU15__autoreleasingP7NSError : 1640 -> 2052
~ +[FIProviderDomain providerDomainForID:cachePolicy:error:] : 112 -> 124
+ __ZN23FIProviderDomainFetcherC2Ev
+ -[FINodeIterator countByEnumeratingWithState:objects:count:]
+ -[FIChildrenIterator countByEnumeratingWithState:objects:count:]
+ -[FINodeIteratorWithExtraChildren countByEnumeratingWithState:objects:count:]
+ -[FICompoundNodeIterator countByEnumeratingWithState:objects:count:]
~ __ZN11TCopyWriter5WriteEv : 5340 -> 5524
~ __ZN11TCopyWriter23WriteExtendedAttributesENSt3__110shared_ptrI9TCopyItemEE : 1904 -> 1936
CStrings:
+ "Lookup of '%{public}@' needed FP's cache, but nothing is monitoring the provider list"
+ "Unwinding after error - %{public}@"
```
