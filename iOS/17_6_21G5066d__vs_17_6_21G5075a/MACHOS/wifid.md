## wifid

> `/usr/sbin/wifid`

```diff

-1682.3.0.0.0
-  __TEXT.__text: 0x180040
+1686.2.0.0.0
+  __TEXT.__text: 0x180af4
   __TEXT.__auth_stubs: 0x2580
-  __TEXT.__objc_stubs: 0x10ba0
+  __TEXT.__objc_stubs: 0x10b80
   __TEXT.__objc_methlist: 0x4f54
-  __TEXT.__objc_methname: 0x160b8
+  __TEXT.__objc_methname: 0x160ae
   __TEXT.__objc_classname: 0x7ab
-  __TEXT.__objc_methtype: 0x2b9f
+  __TEXT.__objc_methtype: 0x2bc5
   __TEXT.__const: 0x8c0
-  __TEXT.__gcc_except_tab: 0x1838
-  __TEXT.__cstring: 0x63eac
+  __TEXT.__gcc_except_tab: 0x1854
+  __TEXT.__cstring: 0x644ec
   __TEXT.__ustring: 0x4c2
   __TEXT.__oslogstring: 0x30d
   __TEXT.__dlopen_cstrs: 0x1a5
   __TEXT.__info_plist: 0x62b
-  __TEXT.__unwind_info: 0x33d0
+  __TEXT.__unwind_info: 0x33e8
   __DATA_CONST.__auth_got: 0x12d0
   __DATA_CONST.__got: 0xfd8
   __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x68f8
-  __DATA_CONST.__cfstring: 0x1ba60
+  __DATA_CONST.__const: 0x6920
+  __DATA_CONST.__cfstring: 0x1bae0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x6a0
+  __DATA_CONST.__objc_classrefs: 0x698
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_intobj: 0xbd0
   __DATA_CONST.__objc_arraydata: 0x378

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0xd500
-  __DATA.__objc_selrefs: 0x4d78
+  __DATA.__objc_selrefs: 0x4d70
   __DATA.__objc_ivar: 0x8b8
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x1048

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 5253
-  Symbols:   1283
-  CStrings:  14820
+  Functions: 5260
+  Symbols:   1282
+  CStrings:  14848
 
Symbols:
- _OBJC_CLASS_$_MSDKManagedDevice
CStrings:
+ "%!s(MISSING) WiFiCC : Could not apply first boot learnt country: [%!@(MISSING)]"
+ "%!s(MISSING) WiFiCC : Initial Post SW Upgrade CountryCode from user defaults : [%!@(MISSING)]"
+ "%!s(MISSING) WiFiCC : Saving Country Code information to initial post SW Upgrade user defaults : [%!@(MISSING)]"
+ "%!s(MISSING) WiFiCC : Saving first boot country code because : initialCountryCodePresent[%!h(MISSING)hu], evaluationCompleteDateRef[%!@(MISSING)], source[%!d(MISSING)], fRRUNewInstallKeyPresent[%!h(MISSING)hu]"
+ "%!s(MISSING) WiFiCC : Successfully applied first learnt country : [%!@(MISSING)] "
+ "%!s(MISSING) WiFiCC: First Boot CC evaluation completed at [%!@(MISSING)]"
+ "%!s(MISSING) WiFiCC: First Boot CC evaluation needed ? : [%!h(MISSING)hu]"
+ "%!s(MISSING) WiFiCC: First Boot CC evaluation pending"
+ "%!s(MISSING) error : [%!d(MISSING)] \n"
+ "%!s(MISSING): WiFiCC : No initial SW upgrade Country Code info present in user defaults"
+ "%!s(MISSING): WiFiCC : Successfully set first boot countrycode: %!@(MISSING) on Power ON\n"
+ "%!s(MISSING): WiFiCC : Timed out trying to determine first boot country code, Evaluation end timestamp being logged [%!@(MISSING)]"
+ "%!s(MISSING): WiFiCC : Trying to determine first boot country code"
+ "%!s(MISSING): WiFiCC : first boot country code evaluation begins at [%!@(MISSING)]"
+ "%!s(MISSING): WiFiCC : first boot country code evaluation end timestamp being logged [%!@(MISSING)]"
+ "-[WiFiLocaleManagerUser setUserDefaultCountryCode:source:]"
+ "-[WiFiLocaleManagerUser setUserDefaultCountryCode:source:]_block_invoke_2"
+ "-[WiFiLocaleManagerUser setUserDefaultCountryCode:source:]_block_invoke_3"
+ "C28@0:8@\"NSString\"16i24"
+ "C28@0:8@16i24"
+ "WiFR-IsNewInstall"
+ "WiFiCC : Could not set first Boot country code"
+ "WiFiCC : Successfully set first Boot country code"
+ "WiFiDeviceManagerCheckMimoEligibility <%!p(MISSING):%!l(MISSING)lu:%!d(MISSING)> \n"
+ "WiFiDeviceManagerSetManufactureDate error<%!d(MISSING):%!p(MISSING):%!p(MISSING)> demo =<%!d(MISSING)>\n"
+ "WiFiDeviceSetMimoEligibility"
+ "WiFiManager-1686.2 Jul 10 2024 02:59:03"
+ "WiFiManager-1686.2 Jul 10 2024 02:59:35"
+ "WiFiManagerGetPostUpgradeCountryCodeFromUserDefaults"
+ "WiFiManagerSaveRecentCountryDataToUserDefaults"
+ "__WiFiManagerDevicePowerCallback"
+ "__WiFiManagerSetFirstBootCountryCodeEvaluationCriteria"
+ "initialCountryCodeEvaluationDate"
+ "initialCountryCodeUserDefault"
+ "initialCountryCodeUserDefaultData"
+ "setUserDefaultCountryCode:source:"
- "-[WiFiLocaleManagerUser setUserDefaultCountryCode:]_block_invoke"
- "Is device a POS Device ? [%!h(MISSING)hu]"
- "WiFiDeviceManagerCheckMimoEligibility error<%!d(MISSING):%!p(MISSING):%!l(MISSING)lu:%!d(MISSING)> \n"
- "WiFiDeviceManagerSetManufactureDate error<%!d(MISSING):%!p(MISSING):%!p(MISSING)> demo =<%!d(MISSING)> pos<%!d(MISSING)>\n"
- "WiFiManager-1682.3 Jun 30 2024 23:34:20"
- "WiFiManager-1682.3 Jun 30 2024 23:34:47"
- "setUserDefaultCountryCode:"
- "typeOfDemoDevice:"

```
