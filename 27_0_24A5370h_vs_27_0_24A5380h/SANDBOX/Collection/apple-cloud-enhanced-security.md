## apple-cloud-enhanced-security

> Group: ⬆️ Updated

```diff

 
 (allow file-clone
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
 		(extension "com.apple.app-sandbox.read-write")
 	)

 		(subpath "/private/var/mobile/tmp/tie-cloud-app")
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/mobile/tmp/tie-cloud-app")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(subpath "/private/var/mobile/tmp/tie-cloud-app")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
 				(require-any
 					(subpath "/private/var/BMCSupport")
 					(subpath "/private/var/BMCSupportInternalAdditions")

 )
 (allow file-read*
 	(require-all
-		(literal "/private")
+		(literal "/private/preboot")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(literal "/private/preboot")
+		(literal "/private")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow file-read-data
 	(require-all
-		(literal "/private")
+		(literal "/private/preboot")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow file-read-data
 	(require-all
-		(literal "/private/preboot")
+		(literal "/private")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 		(extension "com.apple.app-sandbox.read-write")
 	)
 )
+(allow file-write-data
+	(require-all
+		(require-any
+			(literal "/dev/null")
+			(literal "/dev/zero")
+		)
+		(literal "/dev/dtracehelper")
+	)
+)
 (allow file-write-data
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
-(allow file-write-data
-	(require-any
-		(literal "/dev/null")
-		(literal "/dev/zero")
-	)
-)
 
 (deny file-write-setugid)
 

 
 (allow iokit-get-properties
 	(require-all
-		(iokit-property "platform-name")
-		(iokit-registry-entry-class "IOPlatformExpertDevice")
+		(iokit-property "iommu-present")
+		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-property "iommu-present")
-		(iokit-registry-entry-class "IOPlatformDevice")
+		(iokit-property "platform-name")
+		(iokit-registry-entry-class "IOPlatformExpertDevice")
 	)
 )
 (allow iokit-get-properties

 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-property "artwork-scale-factor")
+		(iokit-property "soc-generation")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )

 			(iokit-property "artwork-device-subtype")
 			(iokit-property "artwork-display-gamut")
 			(iokit-property "artwork-dynamic-displaymode")
+			(iokit-property "artwork-scale-factor")
 			(iokit-property "compatible-device-fallback")
 			(iokit-property "device-perf-memory-class")
 			(iokit-property "graphics-featureset-class")

 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "soc-generation")
-		(iokit-registry-entry-class "IOPlatformDevice")
-	)
-)
 
 (allow iokit-open-user-client
 	(extension "com.apple.security.exception.iokit-user-client-class")

 (allow syscall-mig
 	(require-all
 		(require-not (kernel-mig-routine thread_terminate))
-		(require-not (kernel-mig-routine mach_memory_entry_ownership))
-		(require-not (kernel-mig-routine thread_resume))
-		(require-not (kernel-mig-routine mach_port_deallocate))
 		(require-not (kernel-mig-routine thread_suspend))
+		(require-not (kernel-mig-routine mach_port_deallocate))
+		(require-not (kernel-mig-routine thread_resume))
 		(require-not (kernel-mig-routine mach_vm_remap_external))
+		(require-not (kernel-mig-routine mach_memory_entry_ownership))
 		(require-not (state-flag "blastdoor-post-launch"))
 		(require-any
 			(kernel-mig-routine io_service_get_matching_service_bin)

 		(require-any
 			(require-any
 				(sysctl-name "hw.activecpu")
+				(sysctl-name "hw.machine")
+				(sysctl-name "hw.memsize")
 				(sysctl-name "hw.ncpu")
+				(sysctl-name "kern.osproductversion")
 				(sysctl-name "kern.osvariant_status")
 				(sysctl-name "kern.secure_kernel")
 			)

 				(sysctl-name "hw.physicalcpu_max")
 				(sysctl-name "hw.product")
 			)
-			(require-any
-				(sysctl-name "hw.machine")
-				(sysctl-name "kern.osproductversion")
-			)
 			(require-any
 				(sysctl-name "hw.optional.arm.caps")
 				(sysctl-name "hw.optional.neon_fp16")
 			)
 			(require-any
 				(sysctl-name "kern.hostname")
+				(sysctl-name "kern.ostype")
 				(sysctl-name "kern.version")
 			)
 			(require-any
 				(sysctl-name "kern.maxfilesperproc")
 				(sysctl-name "kern.osversion")
 			)
-			(sysctl-name "hw.memsize")
 			(sysctl-name "hw.osenvironment")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")

 			(sysctl-name "kern.bootsessionuuid")
 			(sysctl-name "kern.osrelease")
 			(sysctl-name "kern.osreleasetype")
-			(sysctl-name "kern.ostype")
 			(sysctl-name "machdep.ptrauth_enabled")
 			(sysctl-name "security.mac.lockdown_mode_state")
 			(sysctl-name "vm.malloc_ranges")
```
