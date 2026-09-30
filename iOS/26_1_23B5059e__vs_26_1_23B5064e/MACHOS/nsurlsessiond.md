## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

-3860.200.61.0.0
-  __TEXT.__text: 0x85e70
+3860.200.71.0.0
+  __TEXT.__text: 0x85e60
   __TEXT.__auth_stubs: 0x10c0
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_stubs: 0xa7a0
-  __TEXT.__objc_methlist: 0x618c
+  __TEXT.__objc_stubs: 0xa800
+  __TEXT.__objc_methlist: 0x6194
   __TEXT.__const: 0x278
-  __TEXT.__gcc_except_tab: 0x10854
+  __TEXT.__gcc_except_tab: 0x1084c
   __TEXT.__cstring: 0x3980
-  __TEXT.__objc_methname: 0xf002
+  __TEXT.__objc_methname: 0xf0c8
   __TEXT.__objc_classname: 0xbef
-  __TEXT.__objc_methtype: 0x2e8e
-  __TEXT.__oslogstring: 0xf502
+  __TEXT.__objc_methtype: 0x2eda
+  __TEXT.__oslogstring: 0xf504
   __TEXT.__unwind_info: 0x2dd8
   __DATA_CONST.__auth_got: 0x878
   __DATA_CONST.__got: 0x710

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x8e90
-  __DATA.__objc_selrefs: 0x36a8
+  __DATA.__objc_const: 0x8e98
+  __DATA.__objc_selrefs: 0x36c8
   __DATA.__objc_ivar: 0x704
   __DATA.__objc_data: 0x1630
   __DATA.__data: 0xe4c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3A0609D8-F38F-30C4-9292-FCB1B5CCD911
+  UUID: 771A61F7-B3B4-3081-AFDE-9CE19965BF1C
   Functions: 2067
   Symbols:   494
-  CStrings:  4121
+  CStrings:  4126
 
Functions:
~ sub_100053eec : 3560 -> 3532
~ sub_100054cd4 -> sub_100054cb8 : 1204 -> 1216
CStrings:
+ "NDNWSession <%{public}@> Session <%{public}@> is for <%{public}@>.<%@> using resource timeout: %f, request timeout: %f allowsCellularAccess: %d, allowsExpensiveAccess: %d, allowsConstrainedAccess: %d, _sourceApplicationBundleIdentifier: %{public}@, _sourceApplicationSecondaryIdentifier: %{public}@"
+ "NDSession <%{public}@> Session <%{public}@> is for <%{public}@>.<%@> using resource timeout: %f, request timeout: %f allowsCellularAccess: %d, allowsExpensiveAccess: %d, allowsConstrainedAccess: %d, _sourceApplicationBundleIdentifier: %{public}@, _sourceApplicationSecondaryIdentifier: %{public}@, hasSqliteSupport: %u, allowsUltraConstrainedAccess: %d"
+ "_allowsUltraConstrainedInternal"
+ "_explicitlySetAllowsUCA"
+ "allowsUltraConstrainedNetworkAccess"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "setAllowsUltraConstrainedNetworkAccess:"
+ "set_allowsUltraConstrainedInternal:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "NDNWSession <%{public}@> Session <%{public}@> is for <%{public}@>.<%@> using resource timeout: %f, request timeout: %f allowsCellularAccess: %d, allowsExpensiveAccess: %d, allowsConstrainedAccess: %d, _sourceApplicationBundleIdentifier: %{public}@, _sourceApplicationSecondaryIdentifier: %{public}@, _allowsUCA: %d"
- "NDSession <%{public}@> Session <%{public}@> is for <%{public}@>.<%@> using resource timeout: %f, request timeout: %f allowsCellularAccess: %d, allowsExpensiveAccess: %d, allowsConstrainedAccess: %d, _sourceApplicationBundleIdentifier: %{public}@, _sourceApplicationSecondaryIdentifier: %{public}@, hasSqliteSupport: %u, _allowsUCA: %d"
- "_allowsUCA"
- "_setAllowsUCA:"

```
