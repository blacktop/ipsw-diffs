## libnfstorage.dylib

> `/usr/lib/libnfstorage.dylib`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0x5900
-  __TEXT.__auth_stubs: 0x2d0
+364.20.0.0.0
+  __TEXT.__text: 0x448c
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__objc_methlist: 0x168
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x828
-  __TEXT.__oslogstring: 0x551
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__cstring: 0x6af
+  __TEXT.__oslogstring: 0x416
+  __TEXT.__unwind_info: 0xd8
   __TEXT.__objc_classname: 0xee
-  __TEXT.__objc_methname: 0x8af
+  __TEXT.__objc_methname: 0x894
   __TEXT.__objc_methtype: 0x96
   __TEXT.__objc_stubs: 0xb40
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x310
-  __AUTH_CONST.__auth_got: 0x170
+  __DATA_CONST.__objc_selrefs: 0x308
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x830
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A30C9ABD-F5F0-3A3A-9702-5D30EF815F96
+  UUID: F348320C-0DD3-3947-8B46-32212D46E730
   Functions: 34
-  Symbols:   87
-  CStrings:  260
+  Symbols:   83
+  CStrings:  253
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x26
- _NFLogGetLogger
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x8
- _object_getClass
- _object_getClassName
CStrings:
+ "%{public}s:%i Deleting old DB at %{public}@"
+ "%{public}s:%i Failed to add SQLite store type after removing: %{public}@"
+ "%{public}s:%i Failed to add SQLite store type: %{public}@"
+ "%{public}s:%i Failed to create home directory %{public}@: %{public}@"
+ "%{public}s:%i Failed to delete all: %{public}@"
+ "%{public}s:%i Failed to execute delete request: %{public}@"
+ "%{public}s:%i Failed to execute fetch request: %{public}@"
+ "%{public}s:%i Failed to load model"
+ "%{public}s:%i Failed to save: %{public}@"
+ "%{public}s:%i No applets found in storage"
+ "%{public}s:%i Nothing in DB - return an empty array"
+ "%{public}s:%i Unknown version info %d"
+ "%{public}s:%i Update required; remove entities"
+ "%{public}s:%i Wrong applet storage version %llu, expecting %d"
+ "%{public}s:%i applets: %{public}@"
+ "%{public}s:%i invalid type (%{public}@) for applets"
+ "%{public}s:%i invalid type (%{public}@) for counter"
+ "%{public}s:%i invalid type (%{public}@) for key"
+ "%{public}s:%i invalid type (%{public}@) for seid"
+ "%{public}s:%i managedObjectContext is NULL"
+ "%{public}s:%i new Applet Config=%{public}@"
+ "-[NFStorageController persistentStoreCoordinator]"
+ "-[NFStorageControllerApplet _deleteAllAppletEntities]"
+ "-[NFStorageControllerApplet deleteAllAppletEntities]"
+ "-[NFStorageControllerApplet deleteAllAppletEntities]_block_invoke"
+ "-[NFStorageControllerApplet fetchAppletEntitiesWithError:]"
+ "-[NFStorageControllerApplet fetchAppletEntitiesWithError:]_block_invoke"
+ "-[NFStorageControllerApplet updateAppletEntitiesWithConfig:]"
+ "-[NFStorageControllerApplet updateAppletEntitiesWithConfig:]_block_invoke"
+ "-[NFStorageControllerESEExpress _deleteAllESEExpressEntities]"
+ "-[NFStorageControllerESEExpress deleteAllESEExpressEntities]"
+ "-[NFStorageControllerESEExpress deleteAllESEExpressEntities]_block_invoke"
+ "-[NFStorageControllerESEExpress fetchESEExpressEntitiesWithError:]"
+ "-[NFStorageControllerESEExpress fetchESEExpressEntitiesWithError:]_block_invoke"
+ "-[NFStorageControllerESEExpress updateESEExpressEntitiesWithConfig:]"
+ "-[NFStorageControllerESEExpress updateESEExpressEntitiesWithConfig:]_block_invoke"
- "%c[%{public}s %{public}s]:%i Deleting old DB at %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to add SQLite store type after removing: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to add SQLite store type: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to create home directory %{public}@: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to delete all: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to execute delete request: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to execute fetch request: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to load model"
- "%c[%{public}s %{public}s]:%i Failed to save: %{public}@"
- "%c[%{public}s %{public}s]:%i No applets found in storage"
- "%c[%{public}s %{public}s]:%i Nothing in DB - return an empty array"
- "%c[%{public}s %{public}s]:%i Unknown version info %d"
- "%c[%{public}s %{public}s]:%i Update required; remove entities"
- "%c[%{public}s %{public}s]:%i Wrong applet storage version %llu, expecting %d"
- "%c[%{public}s %{public}s]:%i applets: %{public}@"
- "%c[%{public}s %{public}s]:%i invalid type (%{public}@) for applets"
- "%c[%{public}s %{public}s]:%i invalid type (%{public}@) for counter"
- "%c[%{public}s %{public}s]:%i invalid type (%{public}@) for key"
- "%c[%{public}s %{public}s]:%i invalid type (%{public}@) for seid"
- "%c[%{public}s %{public}s]:%i managedObjectContext is NULL"
- "%c[%{public}s %{public}s]:%i new Applet Config=%{public}@"
- "persistentStoreCoordinator"

```
