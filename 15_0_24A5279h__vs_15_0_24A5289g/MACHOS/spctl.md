## spctl

> `/usr/sbin/spctl`

```diff

-620.0.7.0.0
-  __TEXT.__text: 0xc248
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_stubs: 0xe40
+620.0.16.0.0
+  __TEXT.__text: 0xbd54
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_stubs: 0xea0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x5c4
-  __TEXT.__const: 0x4eb
-  __TEXT.__cstring: 0x182e
-  __TEXT.__objc_methname: 0x1595
+  __TEXT.__objc_methlist: 0x5d4
+  __TEXT.__const: 0x4b3
+  __TEXT.__cstring: 0x1bff
+  __TEXT.__objc_methname: 0x15d3
   __TEXT.__objc_classname: 0xf3
   __TEXT.__objc_methtype: 0x5ef
-  __TEXT.__oslogstring: 0x87c
-  __TEXT.__gcc_except_tab: 0x670
+  __TEXT.__oslogstring: 0x7a7
+  __TEXT.__gcc_except_tab: 0x598
   __TEXT.__dof_security_: 0x28e
-  __TEXT.__unwind_info: 0x4f8
-  __DATA_CONST.__auth_got: 0x4f0
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0xbf8
-  __DATA_CONST.__cfstring: 0xda0
+  __TEXT.__unwind_info: 0x4c0
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0xc38
+  __DATA_CONST.__cfstring: 0xce0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dupclass: 0x58
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x10f8
-  __DATA.__objc_selrefs: 0x530
+  __DATA.__objc_const: 0x1118
+  __DATA.__objc_selrefs: 0x540
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x188

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 327
-  Symbols:   256
-  CStrings:  282
+  Functions: 318
+  Symbols:   244
+  CStrings:  286
 
Symbols:
- __os_assert_log
- __os_crash
- _close
- _fchmod
- _fchown
- _fcopyfile
- _kSecAssessmentUpdateKeyCount
- _kSecAssessmentUpdateKeyRow
- _kSecAssessmentUpdateOperationDisable
- _kSecAssessmentUpdateOperationEnable
- _kSecAssessmentUpdateOperationRemove
- _open
CStrings:
+ "Encountered error when allowing the option to globally disable the assessment system\n"
+ "Encountered error when querying the status of the option to globally disable the assessment system.\n"
+ "Option to globally disable assessment system is %!s(MISSING).\n"
+ "Option to globally disable assessment system is now available in Settings for the next 8 minutes."
+ "System Policy Basic Usage:\n       spctl --assess [--type type] [-v] path ... # assessment\n       spctl --status | --global-disable # system global switch\n\n"
+ "This operation is no longer supported.\n"
+ "This operation is no longer supported. To add an authority, please use configuration profiles.\n"
+ "This operation is no longer supported. To configure the assessment subsystem, please go to Privacy & Security settings or use configuration profiles.\n"
+ "This operation is no longer supported. To disable an authority, please use configuration profiles.\n"
+ "This operation is no longer supported. To disable developer ID-signed software, please use configuration profiles.\n"
+ "This operation is no longer supported. To disable notarized software, please use configuration profiles.\n"
+ "This operation is no longer supported. To disable the assessment subsystem, please use configuration profiles.\n"
+ "This operation is no longer supported. To enable an authority, please use configuration profiles.\n"
+ "This operation is no longer supported. To enable developer ID-signed software, please use configuration profiles.\n"
+ "This operation is no longer supported. To enable notarized software, please use configuration profiles.\n"
+ "This operation is no longer supported. To remove an authority, please use configuration profiles.\n"
+ "allow-disable"
+ "available"
+ "disable-status"
+ "not available"
- "Created rule %!l(MISSING)ld\n"
- "Disabled %!l(MISSING)ld rule(s)\n"
- "Enabled %!l(MISSING)ld rule(s)\n"
- "Removed %!l(MISSING)ld rule(s)\n"
- "System Policy Basic Usage:\n       spctl --assess [--type type] [-v] path ... # assessment\n       spctl --add [--type type] [--path|--requirement|--anchor|--hash] spec ... # add rule(s)\n       spctl [--enable|--disable|--remove] [--type type] [--path|--requirement|--anchor|--hash|--rule] spec # change rule(s)\n       spctl --status | --global-enable | --global-disable # system global switch\n\n"
- "copy system policy defaults"
- "open default database"
- "open target database"
- "set system policy file ownership"
- "set system policy permissions"
- "ui-disable"
- "ui-disable-devid"
- "ui-disable-notarized"
- "ui-enable"
- "ui-enable-devid"
- "ui-enable-notarized"

```
