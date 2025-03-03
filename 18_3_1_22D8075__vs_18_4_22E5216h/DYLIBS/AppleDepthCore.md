## AppleDepthCore

> `/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore`

```diff

-132.4.0.0.0
-  __TEXT.__text: 0x5b378
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x1e6c
-  __TEXT.__const: 0x21b0
-  __TEXT.__gcc_except_tab: 0x52e8
-  __TEXT.__oslogstring: 0x183e
-  __TEXT.__cstring: 0x2f46
-  __TEXT.__unwind_info: 0x1750
-  __TEXT.__objc_classname: 0x43b
-  __TEXT.__objc_methname: 0x50f0
-  __TEXT.__objc_methtype: 0x4155
-  __TEXT.__objc_stubs: 0x31e0
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x148
-  __DATA_CONST.__objc_classlist: 0x128
+137.3.0.0.0
+  __TEXT.__text: 0x5d7b0
+  __TEXT.__auth_stubs: 0x16a0
+  __TEXT.__objc_methlist: 0x2214
+  __TEXT.__const: 0x21d0
+  __TEXT.__gcc_except_tab: 0x58e0
+  __TEXT.__oslogstring: 0x1bb3
+  __TEXT.__cstring: 0x30f7
+  __TEXT.__unwind_info: 0x1868
+  __TEXT.__objc_classname: 0x47f
+  __TEXT.__objc_methname: 0x556f
+  __TEXT.__objc_methtype: 0x3a2f
+  __TEXT.__objc_stubs: 0x3560
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1178
+  __DATA_CONST.__objc_selrefs: 0x1318
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x160
-  __AUTH_CONST.__auth_got: 0xb08
+  __AUTH_CONST.__auth_got: 0xb60
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x190
-  __AUTH_CONST.__cfstring: 0x21c0
-  __AUTH_CONST.__objc_const: 0x3ab0
+  __AUTH_CONST.__const: 0x1d0
+  __AUTH_CONST.__cfstring: 0x2280
+  __AUTH_CONST.__objc_const: 0x3a48
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __DATA.__objc_ivar: 0x264
-  __DATA.__data: 0x1f8
-  __DATA.__bss: 0x1a0
-  __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA.__objc_ivar: 0x294
+  __DATA.__data: 0x210
+  __DATA.__bss: 0x198
+  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 999
-  Symbols:   1562
-  CStrings:  1682
+  Functions: 1011
+  Symbols:   1630
+  CStrings:  1778
 
Symbols:
+ _CVPixelBufferPoolCreate
+ _OBJC_CLASS_$_ADCoreDeviceConfiguration
+ _OBJC_CLASS_$_ADPreferences
+ _OBJC_CLASS_$_ADPreferencesObserver
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_METACLASS_$_ADCoreDeviceConfiguration
+ _OBJC_METACLASS_$_ADPreferences
+ _OBJC_METACLASS_$_ADPreferencesObserver
+ __ZN16PixelBufferUtils21createPixelBufferPoolE6CGSizejm
+ ___NSArray0__struct
+ ___kCFBooleanFalse
+ _class_addMethod
+ _class_addProperty
+ _kADCoreDeviceConfigurationKeyJasperPerformanceEmulatedDevice
+ _kADCoreDeviceConfigurationKeyJasperPerformanceOverridePath
+ _kADCoreDeviceConfigurationKeyVerboseLogs
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferPoolMinimumBufferCountKey
+ _kCVPixelBufferWidthKey
+ _objc_destroyWeak
+ _objc_getAssociatedObject
+ _objc_loadWeakRetained
+ _objc_release_x10
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _objc_setAssociatedObject
+ _objc_storeWeak
CStrings:
+ "\x01\x12\xa1!"
+ "\x05"
+ "!"
+ "%@: (%@)=>(%@)"
+ "%s:%d - ERROR - failed creating pixelBufferPool with error %d"
+ "-[ADImageDescriptor conformedByPixelBuffer:forLayout:]"
+ "/System/AppleInternal/Library/Frameworks/CMCapture.framework/CMCapture"
+ "@\"<ADEspressoRunnerProtocol>\""
+ "@\"ADPreferences\""
+ "@\"NSMutableDictionary\""
+ "@\"NSUserDefaults\""
+ "@\"id\""
+ "@44@0:8@16@?24@32B40"
+ "@48@0:8{CGSize=dd}16Q32@40"
+ "@?"
+ "@@:"
+ "ADCoreDeviceConfiguration"
+ "ADDescriptors.mm"
+ "ADPreferences"
+ "ADPreferencesObserver"
+ "ADStreamSync: stream was initialized with auto aggregation size, but got a non-standard point cloud (%d points)"
+ "B32@0:8^{__CVBuffer=}16Q24"
+ "D"
+ "PixelBuffer has %zu bytes per row in plane %zu, which is not aligned to 64-bytes"
+ "PixelBuffer has %zu bytes per row, which is not aligned to 64-bytes"
+ "PixelBuffer is not backed by IOSurface, so cannot be used as an Espresso buffer"
+ "PixelBuffer with %zu bytes-per-row for plane %zu does not conform to descriptor with bytes-per-row %lu"
+ "PixelBuffer with %zu planes does not conform to descriptor with %lu custom strides"
+ "PixelBuffer with pixel format '%s' does not conform to descriptor with pixel format '%s'"
+ "PixelBuffer with size %dx%d does not conform to descriptor with size %dx%d"
+ "Q24@0:8@16"
+ "Stream sync auto aggregation count set to %zu"
+ "T"
+ "T@\"NSArray\",R,&,N,V_customStrides"
+ "T@\"NSArray\",R,&,N,V_ops"
+ "^B"
+ "__ADPreferencesObserver_%u"
+ "_autoAggregation"
+ "_currentDefaults"
+ "_customStrides"
+ "_domain"
+ "_globalUserDefaults"
+ "_ignoreValueUpdate"
+ "_keys"
+ "_ops"
+ "_originalDefaults"
+ "_preferences"
+ "_updateHandlerBlock"
+ "_userDefaults"
+ "addObserver:forKeyPath:options:context:"
+ "boolForKey:"
+ "boolValue"
+ "cannot set configuration. %{public}@ is set in both global domain and in %@. please only use one."
+ "com.apple.AppleDepthCore"
+ "conformedByPixelBuffer:forLayout:"
+ "createPixelBufferPool"
+ "createPropertyForKey:"
+ "createWithSize:layout:customStrides:"
+ "customStrides"
+ "customStridesForLayout:"
+ "didChangeValueForKey:"
+ "doubleForKey:"
+ "error getting defaults key"
+ "espressoRunnerForPath:forEngine:configurationName:"
+ "expectedNumberOfFramesForObject:"
+ "f24@0:8@16"
+ "failed setting property for configuration key %{public}@"
+ "floatForKey:"
+ "hasPrefix:"
+ "initForPreferences:updateHandlerBlock:keys:invokeOnInit:"
+ "initWithDomain:defaultValues:"
+ "initWithSuiteName:"
+ "integerForKey:"
+ "jasperPerformanceEmulatedDevice"
+ "jasperPerformanceOverridePath"
+ "listForKey:"
+ "null"
+ "numberForKey:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "ops"
+ "planeCount < sizeof(bpps)/sizeof(bpps[0])"
+ "registerUpdateHandlerForKeys:invokeOnRegistration:scopeObject:handlerBlock:"
+ "registerVerbosityConfigurationUpdate"
+ "removeObjectsInRange:"
+ "removeObserver:forKeyPath:context:"
+ "setObject:forKey:"
+ "sharedConfiguration"
+ "standardUserDefaults"
+ "stringByAppendingString:"
+ "stringByReplacingCharactersInRange:withString:"
+ "stringForKey:"
+ "unsignedLongLongValue"
+ "updateValue:forKey:"
+ "v16@?0@\"NSString\"8"
+ "v32@0:8@16@24"
+ "v44@0:8@16B24@28@?36"
+ "v48@0:8@16@24@32^v40"
+ "v@:@"
+ "verboseLogs"
+ "willChangeValueForKey:"
- "\x01\x12\xa1"
- "@\"NSObject<ADEspressoRunnerProtocol>\""
- "resetting dummy operations for espressoV2 runner"
- "{unordered_map<ADLayout, CGSize, std::hash<ADLayout>, std::equal_to<ADLayout>, std::allocator<std::pair<const ADLayout, CGSize>>>=\"__table_\"{__hash_table<std::__hash_value_type<ADLayout, CGSize>, std::__unordered_map_hasher<ADLayout, std::__hash_value_type<ADLayout, CGSize>, std::hash<ADLayout>, std::equal_to<ADLayout>>, std::__unordered_map_equal<ADLayout, std::__hash_value_type<ADLayout, CGSize>, std::equal_to<ADLayout>, std::hash<ADLayout>>, std::allocator<std::__hash_value_type<ADLayout, CGSize>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<ADLayout, std::__hash_value_type<ADLayout, CGSize>, std::hash<ADLayout>, std::equal_to<ADLayout>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<ADLayout, std::__hash_value_type<ADLayout, CGSize>, std::equal_to<ADLayout>, std::hash<ADLayout>>>=\"__value_\"f}}}"

```
