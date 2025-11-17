## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-605.2.5.0.0
-  __TEXT.__text: 0x120730
+605.2.7.0.0
+  __TEXT.__text: 0x120cb0
   __TEXT.__auth_stubs: 0x2260
   __TEXT.__objc_stubs: 0x116a0
   __TEXT.__objc_methlist: 0xa088
-  __TEXT.__const: 0x4a90
+  __TEXT.__const: 0x4aa0
   __TEXT.__gcc_except_tab: 0x2278
   __TEXT.__cstring: 0xd69e
-  __TEXT.__oslogstring: 0x13a90
+  __TEXT.__oslogstring: 0x13c60
   __TEXT.__objc_methname: 0x1bd11
   __TEXT.__objc_classname: 0x1fa7
   __TEXT.__objc_methtype: 0x5586

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D16FBB28-D63C-3057-82D5-6D7387B94F5F
-  Functions: 5984
+  UUID: BF9C7A23-8397-3D5A-83E6-BDC222AD41B6
+  Functions: 5985
   Symbols:   1301
-  CStrings:  8008
+  CStrings:  8012
 
CStrings:
+ "Applying Web Content Filter: isForced=%{bool,public}d, familyMemberType=%{private}s"
+ "Communication Safety forced check: isForced=%{bool,public}d for familyMemberType=%{private}s"
+ "User Safety policy resolved: isRestricted=%{bool,public}d, isForcedToRestricted=%{bool,public}d, familyMemberType=%{private}s, policy=%{public}lld"
+ "Web Content Filter forced to Limit Adult Websites: %{bool,public}d for familyMemberType: %{private}s"

```
