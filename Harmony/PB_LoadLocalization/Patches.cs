using HarmonyLib;
using PhantomBrigade.Mods;
using System.Reflection;
using UnityEngine;

// All mods must use a unique namespace in case they contain colliding type names, like one below
namespace PB_LoadLocalization
{
    // All mods using libraries must include one class inheriting from ModLink
    public class LoadLocalizationLink : ModLink
    {
        public override void OnLoad(Harmony harmonyInstance)
        {
            // Note that you have access to metadata, which includes directory name and full path to this loaded mod.
            // You can also access ModManager.loadedModsLookup to find other loaded mods and interact with them (e.g. if you're relying on another mod)
            Assembly executingAssembly = Assembly.GetExecutingAssembly();
            Debug.Log("Mod " + metadata.id + " is executing OnLoad | Using HarmonyInstance.PatchAll on assembly (" + executingAssembly.FullName + ") | Directory: " + metadata.directory + " | Full path: " + metadata.path);
            harmonyInstance.PatchAll(executingAssembly);
        }
    }

    // Container class for patches - useful if you prefer to keep patches organized under one umbrella type
    public class Patches
    {
        [HarmonyPatch(typeof(CIViewSplashScreen))]
        [HarmonyPatch("TryExit")]
        public class PatchOnCIViewSplashScreenTryExit
        {
            // The process below is executed after CIViewSplashScreen.TryExit() closes the splash screens waiting for the game to start, including the Seizure Warning and Wwise credit.
            public static void Postfix()
            {
                Debug.Log("<PB_LoadLocalization> Mod executes this as suffix to CIViewSplashScreen.TryExit()");

                PhantomBrigade.DebugConsole.ConsoleCommandsData.UpdateLocalization();
            }
        }
    }
}