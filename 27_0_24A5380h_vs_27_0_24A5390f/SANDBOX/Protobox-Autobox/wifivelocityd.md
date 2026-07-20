## wifivelocityd

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AppleBCMWLANSkywalkInterface")
 		(iokit-registry-entry-class "AppleKeyStore")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.cfprefs.daemonv1")

 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	)
 )
 
+(deny process-codesigning
+	(require-all
+		(require-not (literal "/usr/bin/sw_vers"))
+		(require-not (require-any
+			(literal "/sbin/ifconfig")
+			(literal "/sbin/ping6")
+			(literal "/usr/bin/dns-sd")
+			(literal "/usr/bin/footprint")
+			(literal "/usr/bin/heap")
+			(literal "/usr/bin/vmmap")
+			(literal "/usr/sbin/arp")
+			(literal "/usr/sbin/ndp")
+			(literal "/usr/sbin/netstat")
+			(literal "/usr/sbin/scutil")
+			(literal "/usr/sbin/traceroute")
+		))
+		(require-any
+			(require-all
+				(require-not (literal "/usr/sbin/kextstat"))
+				(require-not (require-any
+					(literal "/usr/bin/zprint")
+					(literal "/usr/sbin/ioreg")
+				))
+				(require-not (literal "/sbin/ping"))
+				(require-not (literal "/usr/bin/log"))
+				(require-not (literal "/bin/sh"))
+				(require-not (literal "/usr/sbin/tcpdump"))
+			)
+			(require-all
+				(system-attribute internal-build)
+				(require-not (require-any
+					(literal "/usr/local/bin/3bars")
+					(literal "/usr/local/bin/curl")
+					(literal "/usr/local/bin/dnssdutil")
+					(literal "/usr/local/bin/easyperf")
+					(literal "/usr/local/bin/mobilewifitool")
+					(literal "/usr/local/bin/security")
+					(literal "/usr/local/bin/wifistats")
+					(literal "/usr/local/bin/wl")
+				))
+				(require-not (literal "/usr/local/bin/profilectl"))
+				(require-not (literal "/usr/local/bin/jetsam_priority"))
+				(require-not (literal "/usr/local/bin/apple80211"))
+				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (literal "/usr/sbin/kextstat"))
+				(require-not (require-any
+					(literal "/usr/bin/zprint")
+					(literal "/usr/sbin/ioreg")
+				))
+				(require-not (literal "/sbin/ping"))
+				(require-not (literal "/usr/bin/log"))
+				(require-not (literal "/bin/sh"))
+				(require-not (literal "/usr/sbin/tcpdump"))
+			)
+		)
+	)
+)
+
 (deny process-exec*
 	(require-all
 		(require-not (literal "/usr/bin/sw_vers"))

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
