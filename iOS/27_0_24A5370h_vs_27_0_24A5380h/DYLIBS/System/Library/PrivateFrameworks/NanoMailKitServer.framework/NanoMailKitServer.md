## NanoMailKitServer

> `/System/Library/PrivateFrameworks/NanoMailKitServer.framework/NanoMailKitServer`

```diff

-  __TEXT.__text: 0x787c4
+  __TEXT.__text: 0x7874c
   __TEXT.__objc_methlist: 0x94dc
   __TEXT.__const: 0x5b6
   __TEXT.__cstring: 0x4b97
-  __TEXT.__oslogstring: 0x826f
+  __TEXT.__oslogstring: 0x8223
   __TEXT.__gcc_except_tab: 0x308
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1818
+  __TEXT.__unwind_info: 0x1810
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d10
+  __DATA_CONST.__objc_selrefs: 0x3d08
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x560
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x6500
-  __AUTH_CONST.__objc_const: 0xe4d8
+  __AUTH_CONST.__objc_const: 0xe4d0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3296
-  Symbols:   10214
+  Functions: 3295
+  Symbols:   10211
   CStrings:  2095
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[NNMKSyncStateManager registry:didDeactivate:]
- -[NNMKSyncProvider syncStateManagerDidUnpair:]
- ___46-[NNMKSyncProvider syncStateManagerDidUnpair:]_block_invoke
- _objc_msgSend$syncStateManagerDidUnpair:
Functions:
~ -[NNMKSyncStateManager pairingStorePath] : 84 -> 76
+ -[NNMKSyncStateManager registry:didActivate:]
- ___46-[NNMKSyncProvider syncStateManagerDidUnpair:]_block_invoke
- ___58-[NNMKSyncProvider syncStateManagerDidChangePairedDevice:]_block_invoke
CStrings:
+ "Received Activate notification from PDRRegistry. Informing NNMKSyncProvider..."
+ "Received Deactivate notification from PDRRegistry. Informing NNMKSyncProvider..."
- "#PAIRING_STATE Unpairing detected. Triggering verification to insure we don't stop sync'ing if we still have another device we're talking to..."
- "Received Paired Device Changed notification from PDRRegistry. Informing NNMKSyncProvider..."

```
