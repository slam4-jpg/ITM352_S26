def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress


def test_determine_progress(progress_function):
    """
    Test function for determine_progress1 using assert statements.
    
    Test cases cover all four possible return values:
    1. "Get going!" - when spins = 0 (edge case)
    2. "Get going!" - when hits/spins <= 0 (ratio of 0)
    3. "On your way!" - when 0 < ratio < 0.25
    4. "Almost there!" - when 0.25 <= ratio < 0.5
    5. "You win!" - when ratio >= 0.5 and hits < spins
    """
    # Test case 1: spins = 0 returns "Get going!"
    assert progress_function(10, 0) == "Get going!", "Test case 1 failed: spins = 0"
    
    # Test case 2: hits/spins = 0 returns "Get going!"
    assert progress_function(0, 10) == "Get going!", "Test case 2 failed: hits/spins = 0"
    
    # Test case 3: hits/spins = 0.1 (0 < ratio < 0.25) returns "On your way!"
    assert progress_function(1, 10) == "On your way!", "Test case 3 failed: hits/spins = 0.1"
    
    # Test case 4: hits/spins = 0.25 (ratio >= 0.25) returns "Almost there!"
    assert progress_function(1, 4) == "Almost there!", "Test case 4 failed: hits/spins = 0.25"
    
    # Test case 5: hits/spins = 0.4 (0.25 <= ratio < 0.5) returns "Almost there!"
    assert progress_function(4, 10) == "Almost there!", "Test case 5 failed: hits/spins = 0.4"
    
    # Test case 6: hits/spins = 0.5 but hits >= spins returns "Almost there!"
    assert progress_function(5, 10) == "Almost there!", "Test case 6 failed: hits/spins = 0.5 with hits < spins"
    
    # Test case 7: hits/spins = 0.6 with hits < spins returns "You win!"
    assert progress_function(6, 10) == "You win!", "Test case 7 failed: hits/spins = 0.6 with hits < spins"
    
    # Test case 8: hits/spins = 0.5 with hits < spins returns "You win!"
    assert progress_function(5, 11) == "You win!", "Test case 8 failed: hits/spins = 0.5 with hits < spins"
    
    print("✓ All tests passed!")


# Run the test
if __name__ == "__main__":
    test_determine_progress(determine_progress1)


def determine_progress2(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    progress = "Get going!"
    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5 and hits < spins:
                progress = "You win!"

    return progress

def test_determine_progress2(progress_function):
    #test case 1: spins = 0 returns "Get going!"
    assert progress_function(10, 0) == "Get going!", "Test case
    assert progress_function(2,5) == "On your way!", "Test case 2 failed: hits/spins = 0.4"
    assert progress_function(1,4) == "Almost there!", "Test case 3 failed: hits/spins = 0.25"
    assert progress_function(6,10) == "You win!", "Test case 4 failed: hits/spins = 0.6 with hits < spins"
    assert progress_function(5,10) == "Almost there!", "Test case 5 failed: hits/spins = 0.5 with hits < spins"
    assert progress_function(5,11) == "You win!", "Test case 6 failed: hits/spins = 0.5 with hits < spins"

    test_determine_progress2(determine_progress2) 


def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    progress = "Get going!"
    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5 and hits < spins:
                progress = "You win!"

    return "Almost there!" 

def test_determine_progress3(progress_function):
    assert progress_function(10, 0) == "Get going!", "Test case 1 failed: spins = 0"
    assert progress_function(2,5) == "On your way!", "Test case 2 failed: hits/spins = 0.4"
    assert progress_function(1,4) == "Almost there!", "Test case 3 failed: hits/spins = 0.25"
    assert progress_function(6,10) == "You win!", "Test case 4 failed: hits/spins = 0.6 with hits < spins"
    assert progress_function(5,10) == "Almost there!", "Test case 5 failed: hits/spins = 0.5 with hits < spins"
    assert progress_function(5,11) == "You win!", "Test case 6 failed: hits/spins = 0.5 with hits < spins"

    test_determine_progress3(determine_progress3)


def determine_progress4(hits, spins):
    if spins == 0:
        return "Get going!"
# create a list of progress messages in order
progress_messages = ["Get going!", "On your way!", "Almost there!", "You win!"]

# calculate index based on conditions 
index = 0
index += 1* (hits_spins_ratio > 0  )
index += 1* (hits_spins_ratio >= 0.25)
index += 1* (hits_spins_ratio >= 0.5 and hits < spins)

# if ratio >= 0.5 and hits < spins, we need to go back to "Almost there!" instead of "You win!"

index -= 1* (hits_spins_ratio >= 0.5 and hits <= spins and index ==3)

return progress_messages[index] 

test_determine_progress