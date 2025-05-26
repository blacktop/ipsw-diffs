## ContactsSettings

> `/System/Library/PreferenceBundles/ContactsSettings.bundle/ContactsSettings`

```diff

-1239.1.0.0.0
+1240.6.1.0.0
   __TEXT.__text: 0x5cac
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__objc_methlist: 0x3cc
-  __TEXT.__cstring: 0x5ff
+  __TEXT.__cstring: 0x5fc
   __TEXT.__oslogstring: 0x1f0
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x19c
   __TEXT.__unwind_info: 0x1f4
-  __TEXT.__objc_classname: 0x112
-  __TEXT.__objc_methname: 0x189d
-  __TEXT.__objc_methtype: 0x4d5
+  __TEXT.__objc_classname: 0x111
+  __TEXT.__objc_methname: 0x18ab
+  __TEXT.__objc_methtype: 0x4d4
   __TEXT.__objc_stubs: 0x14e0
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x190

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xba0
   __DATA_CONST.__objc_selrefs: 0x650
+  __DATA_CONST.__objc_classrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__cfstring: 0x660
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__auth_got: 0x3f0
   __AUTH.__data: 0x10
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_classrefs: 0x108
-  __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x240
   __DATA.__bss: 0x50

   - /usr/lib/libobjc.A.dylib
   Functions: 124
   Symbols:   727
-  CStrings:  417
+  CStrings:  418
 
Symbols:
+ -[ContactProviderController .cxx_destruct]
+ -[ContactProviderController init]
+ -[ContactProviderController provider]
+ -[ContactProviderController readToggleSwitchSpecifierValue:]
+ -[ContactProviderController setProvider:]
+ -[ContactProviderController setToggleSwitchSpecifierValue:specifier:]
+ -[ContactProviderController specifiers]
+ -[ContactsSettingsPlugin contactProviderCount:]
+ _CNContactProviderEnabled
+ _OBJC_CLASS_$_CNContactProvider
+ _OBJC_CLASS_$_ContactProviderController
+ _OBJC_IVAR_$_ContactProviderController._provider
+ _OBJC_METACLASS_$_ContactProviderController
+ __OBJC_$_INSTANCE_METHODS_ContactProviderController
+ __OBJC_$_INSTANCE_VARIABLES_ContactProviderController
+ __OBJC_$_PROP_LIST_ContactProviderController
+ __OBJC_CLASS_RO_$_ContactProviderController
+ __OBJC_METACLASS_RO_$_ContactProviderController
+ ___39-[ContactProviderController specifiers]_block_invoke
+ ___47-[ContactsSettingsPlugin contactProviderCount:]_block_invoke
+ ___47-[ContactsSettingsPlugin contactProviderCount:]_block_invoke_2
+ ___69-[ContactProviderController setToggleSwitchSpecifierValue:specifier:]_block_invoke
+ ___69-[ContactProviderController setToggleSwitchSpecifierValue:specifier:]_block_invoke_2
- -[ContactsProviderController .cxx_destruct]
- -[ContactsProviderController init]
- -[ContactsProviderController provider]
- -[ContactsProviderController readToggleSwitchSpecifierValue:]
- -[ContactsProviderController setProvider:]
- -[ContactsProviderController setToggleSwitchSpecifierValue:specifier:]
- -[ContactsProviderController specifiers]
- -[ContactsSettingsPlugin contactsProviderCount:]
- _CNContactsProviderEnabled
- _OBJC_CLASS_$_CNContactsProvider
- _OBJC_CLASS_$_ContactsProviderController
- _OBJC_IVAR_$_ContactsProviderController._provider
- _OBJC_METACLASS_$_ContactsProviderController
- __OBJC_$_INSTANCE_METHODS_ContactsProviderController
- __OBJC_$_INSTANCE_VARIABLES_ContactsProviderController
- __OBJC_$_PROP_LIST_ContactsProviderController
- __OBJC_CLASS_RO_$_ContactsProviderController
- __OBJC_METACLASS_RO_$_ContactsProviderController
- ___40-[ContactsProviderController specifiers]_block_invoke
- ___48-[ContactsSettingsPlugin contactsProviderCount:]_block_invoke
- ___48-[ContactsSettingsPlugin contactsProviderCount:]_block_invoke_2
- ___70-[ContactsProviderController setToggleSwitchSpecifierValue:specifier:]_block_invoke
- ___70-[ContactsProviderController setToggleSwitchSpecifierValue:specifier:]_block_invoke_2
CStrings:
+ "@\"CNContactProvider\""
+ "ContactProvider"
+ "ContactProviderController"
+ "ContactProviderSpacer"
+ "T@\"CNContactProvider\",&,N,V_provider"
+ "T@\"NSString\",?,R,C"
+ "contactProviderCount:"
+ "contact_provider"
- "@\"CNContactsProvider\""
- "ContactsProvider"
- "ContactsProviderController"
- "ContactsProviderSpacer"
- "T@\"CNContactsProvider\",&,N,V_provider"
- "contactsProviderCount:"
- "contacts_provider"

```
