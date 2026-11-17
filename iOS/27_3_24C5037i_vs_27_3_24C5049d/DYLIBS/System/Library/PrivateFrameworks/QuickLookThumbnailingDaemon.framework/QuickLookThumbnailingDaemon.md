## QuickLookThumbnailingDaemon

> `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon`

```diff

-218.1.3.200.0
-  __TEXT.__text: 0x53038
+218.3.2.0.0
+  __TEXT.__text: 0x531ac
   __TEXT.__objc_methlist: 0x326c
-  __TEXT.__const: 0x1014
+  __TEXT.__const: 0x1004
   __TEXT.__gcc_except_tab: 0xc80
   __TEXT.__cstring: 0x42e6
-  __TEXT.__oslogstring: 0x5645
+  __TEXT.__oslogstring: 0x5675
   __TEXT.__constg_swiftt: 0x400
   __TEXT.__swift5_typeref: 0xac2
   __TEXT.__swift5_builtin: 0x78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2040
+  Functions: 2041
   Symbols:   2739
-  CStrings:  878
+  CStrings:  879
 
Symbols:
+ -[QLServerThread _saveLargeThumbnailToGenstoreWithData:url:writeAccessURL:]
- -[QLServerThread _saveLargeThumbnailToGenstoreWithData:url:]
CStrings:
+ "No explicit write access for the GenStore write to %@"
```
