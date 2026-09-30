## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-2003.200.33.2.5
-  __TEXT.__text: 0x1b31e8
-  __TEXT.__objc_methlist: 0xdc44
+2003.200.44.0.0
+  __TEXT.__text: 0x1b3ab0
+  __TEXT.__objc_methlist: 0xdc64
   __TEXT.__const: 0x6108
-  __TEXT.__cstring: 0x11b56
-  __TEXT.__oslogstring: 0x1bdf8
+  __TEXT.__cstring: 0x11bb6
+  __TEXT.__oslogstring: 0x1c0d8
   __TEXT.__gcc_except_tab: 0x3de0
   __TEXT.__ustring: 0xac
   __TEXT.__dlopen_cstrs: 0x102

   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x8f90
+  __TEXT.__unwind_info: 0x8fa0
   __TEXT.__eh_frame: 0x33d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5420
+  __DATA_CONST.__const: 0x5438
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d50
+  __DATA_CONST.__objc_selrefs: 0x6d68
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__got: 0x1ad0
   __AUTH_CONST.__const: 0x55a8
-  __AUTH_CONST.__cfstring: 0x7740
-  __AUTH_CONST.__objc_const: 0x3da18
+  __AUTH_CONST.__cfstring: 0x77a0
+  __AUTH_CONST.__objc_const: 0x3da28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0x588
+  __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__auth_got: 0x1ec8
-  __AUTH.__objc_data: 0x2168
+  __AUTH.__objc_data: 0x1bf0
   __AUTH.__data: 0x1598
   __DATA.__objc_ivar: 0xdf4
-  __DATA.__data: 0x2958
+  __DATA.__data: 0x2948
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1b80
+  __DATA_DIRTY.__objc_data: 0x20f8
   __DATA_DIRTY.__bss: 0x3c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9514
-  Symbols:   1877
-  CStrings:  3892
+  Functions: 9517
+  Symbols:   1880
+  CStrings:  3908
 
Symbols:
+ _IDSDataChannelDrainingLinkKey
+ _IDSDataChannelDrainingReasonKey
+ _IDSDataChannelPreferenceSupportsLinkDrainingKey
CStrings:
+ "<%@> Can't find the linkContext of draining linkID %u"
+ "<%@> Can't find the linkContext of un-draining linkID %u"
+ "<%@> IDSDataChannelPreferenceSupportsLinkDrainingKey - client %s link draining"
+ "<%@> sent IDSDataChannelEventLinkDrainCancelled, linkID %u"
+ "<%@> sent IDSDataChannelEventLinkDraining, linkID %u, reason: %d"
+ "cancelDrainOfIDSDataChannelLinkContext: connection already closed"
+ "does not support"
+ "drainIDSDataChannelLinkContext: connection already closed"
+ "draining-link-key"
+ "draining-reason"
+ "got drain-cancelled linkID %d, linkUUID %@ (reason byte %d, unused)"
+ "got drainingLinkID %d, linkUUID %@, reason: %d"
+ "kClientChannelMetadataType_LinkDrainCancelled should be %d byte, not %u bytes, field: %u"
+ "kClientChannelMetadataType_LinkDraining should be %d byte, not %u bytes, field: %u"
+ "preference-supports-link-draining"
+ "supports"
```
